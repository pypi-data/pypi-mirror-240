from enot.latency.search_space_latency_container import SearchSpaceLatencyContainer
from typing import Optional, Tuple

def plot_latency_heatmap(container: SearchSpaceLatencyContainer, annotate_values: bool = ..., figsize: Optional[Tuple[int, int]] = ...):
    """
    Plots latencies of operations by blocks.

    Parameters
    ----------
    container : SearchSpaceLatencyContainer
        Container for visualization.
    annotate_values : bool, optional
        Whether to print probability values over the heatmap (the default
        is False).
    figsize : tuple with two ints or None, optional
        Figure size (the default is None, which uses default matplotlib
        figure size).

    Returns
    -------
    matplotlib.pylab.Figure

    """
