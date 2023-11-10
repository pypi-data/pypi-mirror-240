from enot.models import SearchSpaceModel
from typing import List, Optional, Union

def min_latency(arg) -> float:
    """Sum of minimum latencies over all containers supplemented by constant part."""
def max_latency(arg) -> float:
    """Sum of maximum latencies over all containers supplemented by constant part."""
def mean_latency(arg) -> float:
    """Sum of mean latencies over all containers supplemented by constant part."""
def median_latency(arg, n: int = ...) -> float:
    """Compute median latency of n sampled architectures of :class:`.SearchSpaceModel` or
    :class:`.SearchSpaceLatencyContainer`."""
def current_latency(arg, arch: Optional[List[Union[List[int], int]]] = ...) -> float:
    """Returns current latency of :class:`.SearchSpaceModel` or :class:`.SearchSpaceLatencyContainer`."""
def best_arch_latency(search_space: SearchSpaceModel) -> float:
    """
    Returns latency of best architecture of search space.

    Parameters
    ----------
    search_space : SearchSpaceModel
        SearchSpaceModel for calculating latency of best architecture.
        Best architecture is taken from search space.

    Returns
    -------
    float

    """
def sample_latencies(arg, n: int = ...) -> List[float]:
    """Returns latencies of n sampled architectures of :class:`.SearchSpaceModel`
    or :class:`.SearchSpaceLatencyContainer`."""
