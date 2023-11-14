import dataclasses 
from typing import List, Optional, Tuple

from constants import ndarray
import jax.numpy as np 
import jax.random as npr 
from jax.scipy.stats import multivariate_normal
from jax import vmap
import jax 

@dataclasses.dataclass 
class KMeansConfig: 
    num_clusters: int 
    max_iterations: Optional[int]=100
    convergence_tolerance: Optional[float]=1e-03 
    initialization_method: Optional[str]="random_from_data"

class KMeans: 
    def __init__(self, config: KMeansConfig): 
        self.config = config 
        self.num_clusters = self.config.num_clusters
        self.objective_history: List[float]  = [] 

    def initialize(self, key: ndarray, x: ndarray, **kwargs): 
        num_samples: int = x.shape[0]
        dimension: int = x.shape[-1] 
        if self.config.initialization_method == "random_from_data": 
            self.means: ndarray = x[npr.choice(key, np.arange(num_samples), shape=(self.num_clusters,), replace=False), :]
        else: 
            raise NotImplementedError

    def fit(self, x: ndarray) -> None: 
        current_objective: float = self.objective(self.means, x) 
        assignments: ndarray = np.argmin(np.linalg.norm(x[:, None, :] - self.means[None, ...], axis=-1), axis=1)

        def body(carried_state: Tuple[Tuple[ndarray], Tuple[ndarray]]) -> Tuple[Tuple[ndarray], Tuple[ndarray]]: 
            (means, _), (previous_objective, current_objective), (num_iterations,)= carried_state
            assignments: ndarray = np.argmin(np.linalg.norm(x[:, None, :] - means[None, ...], axis=-1), axis=1)
            means = vmap(lambda i: np.mean(x, axis=0, where=(assignments == i)[:, None]))(np.arange(self.num_clusters))
            previous_objective = current_objective 
            current_objective = self.objective(means, x) 
            return (means, assignments), (previous_objective, current_objective), (num_iterations + 1,)

        def cond(carried_state) -> bool: 
            (_, _), (previous_objective, current_objective), (num_iterations,) = carried_state 
            return np.logical_or(np.linalg.norm(current_objective - previous_objective) > self.config.convergence_tolerance, num_iterations < self.config.max_iterations)

        initial_state = ((self.means, assignments), (np.inf, self.objective(self.means, x)), (0,))
        (self.means, assignments), (_, _), (self.num_iterations,) = jax.lax.while_loop(cond, body, initial_state)
        self.converged = self.num_iterations < self.config.max_iterations

    def objective(self, x: ndarray, means: ndarray) -> ndarray: 
        return np.linalg.norm((x[:, None, :] - means[None, ...]), axis=-1).sum() 

@dataclasses.dataclass 
class MixtureModelConfig: 
    num_clusters: int 
    max_iterations: Optional[int]=100
    convergence_tolerance: Optional[float]=1e-03 
    covariance_regularization: Optional[float]=1e-06 
    covariance_type: Optional[str]="full"
    num_initializations: Optional[int]=1 
    initialization_method: Optional[str]="random_from_data"

class MixtureModel: 
    def __init__(self, config: MixtureModelConfig): 
        self.config = config 
        self.num_clusters: int = self.config.num_clusters
        self.log_likelihood_history: List[float] = [] 

    @property 
    def num_parameters(self) -> int: 
        dimension: int = self.means.shape[-1] 
        covariance_params: int = self.num_clusters * dimension * (dimension + 1) / 2.
        mean_params: int = self.num_clusters * dimension
        return int(mean_params + covariance_params + self.num_clusters - 1) 

    @property 
    def aic(self, x: ndarray) -> float: 
        return 2 * self.num_parameters() - 2 * self.log_likelihood(x) * x.shape[0] 

    def initialize(self, key: ndarray, x: ndarray, **kwargs): 
        num_samples: int = x.shape[0]
        dimension: int = x.shape[-1] 
        mean_key, covariance_key, weight_key = npr.split(key, 3) 

        if self.config.initialization_method == "random_from_data": 
            self.means: ndarray = x[npr.choice(mean_key, np.arange(num_samples), shape=(self.num_clusters,), replace=False), :]
        elif self.config.initialization_method == "kmeans": 
            config = KMeansConfig(num_clusters=self.num_clusters, max_iterations=self.config.max_iterations)
            kmeans = KMeans(config)
            kmeans.initialize(mean_key, x)
            kmeans.fit(x)
            self.means = kmeans.means 
        else: 
            raise NotImplementedError

        if self.config.covariance_type == "full": 
            sample_covariance: callable = lambda key: np.diag(npr.uniform(key, shape=(dimension,), minval=1., maxval=3.))
            covariance_keys: ndarray = npr.split(covariance_key, self.num_clusters)
            self.covariances: ndarray = vmap(sample_covariance)(covariance_keys)
        else: 
            raise NotImplementedError

        self.cluster_weights: ndarray = np.ones(self.num_clusters) / self.num_clusters
        self.responsibilities: ndarray = np.zeros((num_samples, self.num_clusters))

    def expectation_iteration(self, x: ndarray) -> None: 
        def compute_responsibility(x: ndarray) -> ndarray: 
            cluster_likelihoods: ndarray = vmap(multivariate_normal.pdf, in_axes=(None, 0, 0))(x, self.means, self.covariances)
            return (self.cluster_weights * cluster_likelihoods) / (self.cluster_weights @ cluster_likelihoods)

        self.responsibilities = vmap(compute_responsibility)(x) 

    def maximization_iteration(self, x: ndarray) -> None: 
        total_responsibilities: ndarray = self.responsibilities.sum(0)
        
        def mean_update(cluster_id: int) -> ndarray: 
            responsibilities: ndarray = self.responsibilities[:, cluster_id] 
            return (responsibilities @ x) / total_responsibilities[cluster_id] 

        self.means = vmap(mean_update)(np.arange(self.num_clusters))

        def covariance_update(cluster_id: int) -> ndarray: 
            responsibilities: ndarray = self.responsibilities[:, cluster_id] 
            def point_update(x: ndarray, responsibility: ndarray) -> ndarray: 
                return responsibility * np.outer(x - self.means[cluster_id], x - self.means[cluster_id])
            return vmap(point_update)(x, responsibilities).sum(axis=0) / total_responsibilities[cluster_id] 
            
        self.covariances = vmap(covariance_update)(np.arange(self.num_clusters))
        num_points: int = x.shape[0] 
        self.cluster_weights = total_responsibilities / num_points


    def fit(self, x: ndarray) -> None: 
        self.converged = False
        self.current_log_likelihood: ndarray = self.log_likelihood(x)
        self.log_likelihood_history.append(self.current_log_likelihood)
        self.num_iterations: int = 0 

        for i in range(self.config.max_iterations): 
            self.expectation_iteration(x)
            self.maximization_iteration(x)

            self.previous_log_likelihood = self.current_log_likelihood 
            self.current_log_likelihood = self.log_likelihood(x)
            self.log_likelihood_history.append(self.current_log_likelihood)

            if np.abs(self.previous_log_likelihood - self.current_log_likelihood) < self.config.convergence_tolerance: 
                self.converged = True
                break 

        self.num_iterations = i 

    def log_likelihood(self, x: ndarray) -> ndarray: 
        def cluster_log_likelihood(x: ndarray, mean: ndarray, covariance: ndarray) -> ndarray: 
            return vmap(multivariate_normal.pdf, in_axes=(0, None, None))(x, mean, covariance).sum()
        return self.cluster_weights @ np.log(vmap(cluster_log_likelihood, in_axes=(None, 0, 0))(x, self.means, self.covariances))
