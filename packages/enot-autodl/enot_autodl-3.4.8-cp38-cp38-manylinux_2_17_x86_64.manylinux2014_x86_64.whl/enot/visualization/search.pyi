import numpy as np
from typing import List, Optional, Tuple, Union

def plot_probability_heatmap(probabilities: Union[List[List[float]], np.ndarray], annotate_values: bool = ..., figsize: Optional[Tuple[int, int]] = ...):
    """
    Plots probabilities of operations by blocks.

    Parameters
    ----------
    probabilities : list of list of floats or ndarray
        Probabilities for visualization.
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
