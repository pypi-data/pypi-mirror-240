from enot.latency.search_space_latency_container import SearchSpaceLatencyContainer

def check_is_latency_container(latency_container: SearchSpaceLatencyContainer) -> None:
    """
    Checks that latency container is an instance of SearchSpaceLatencyContainer.

    Parameters
    ----------
    latency_container : SearchSpaceLatencyContainer
        Latency container to check.

    Raises
    ------
    TypeError
        If latency container is not an instance of SearchSpaceLatencyContainer.

    """
def check_latency_value(latency: float) -> None:
    """
    Checks that latency is a positive floating point number.

    Parameters
    ----------
    latency : float
        Latency value to check.

    Raises
    ------
    TypeError
        If latency value is not a floating point number.
    ValueError
        If latency value is not positive.

    """
def check_latency_is_achievable(latency_container: SearchSpaceLatencyContainer, latency: float) -> None:
    """
    Checks that latency if satisfiable.

    Checks that there exists a combination of operations in the latency container which total latency is smaller than
    the provided latency.

    Parameters
    ----------
    latency_container : SearchSpaceLatencyContainer
        Latency container to compare latency with.
    latency : float
        Latency value to test.

    Raises
    ------
    ValueError
        If latency value is lower than the latency of the fastest architecture for the corresponding latency container.

    """
