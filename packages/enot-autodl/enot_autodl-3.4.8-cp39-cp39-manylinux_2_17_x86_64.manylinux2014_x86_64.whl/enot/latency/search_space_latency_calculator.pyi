import abc
from abc import ABC, abstractmethod
from enot.latency.search_space_latency_container import SearchSpaceLatencyContainer
from enot.models import SearchSpaceModel
from typing import Any, Dict, Optional, Tuple

class SearchSpaceLatencyCalculator(ABC, metaclass=abc.ABCMeta):
    """Search space latency calculator interface."""
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None:
        """
        Inits :class:`.SearchSpaceLatencyCalculator` with :class:`.SearchSpaceModel`.

        Parameters
        ----------
        search_space : SearchSpaceModel
            SearchSpaceModel for latency calculation.
        **kwargs
            Arbitrary keyword arguments for SearchSpaceLatencyCalculator.

        """
    @abstractmethod
    def compute(self, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ...) -> SearchSpaceLatencyContainer:
        """
        Computes latency of :class:`.SearchSpaceModel`.

        Parameters
        ----------
        inputs : Tuple
            Model input.
        keyword_inputs : Optional[Dict[str, Any]]
            Model keyword input arguments.

        Returns
        -------
        SearchSpaceLatencyContainer

        """

class SearchSpaceCommonCalculator(SearchSpaceLatencyCalculator):
    """
    Search space common latency calculator.

    The calculator is based on third-party calculators.

    """
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None: ...
    def compute(self, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ...) -> SearchSpaceLatencyContainer: ...

class SearchSpaceMacThopCalculator(SearchSpaceCommonCalculator):
    """Search space MAC calculator based on **thop** third-party calculator."""
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None: ...

class SearchSpaceMacPthflopsCalculator(SearchSpaceCommonCalculator):
    """Search space MAC calculator based on **pthflops** third-party calculator."""
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None: ...

class SearchSpaceMacFvcoreCalculator(SearchSpaceCommonCalculator):
    """Search space MAC calculator based on **fvcore** third-party calculator."""
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None: ...

class SearchSpacePytorchLatencyCalculator(SearchSpaceLatencyCalculator):
    """
    Pytorch latency calculator for :class:`.SearchSpaceModel`.

    Calculator measures latency (time in ms) of :class:`.SearchSpaceModel`
    and supports two types of devices: ``cpu`` and ``cuda``.

    """
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None:
        """
        Parameters
        ----------
        search_space : SearchSpaceModel
            SearchSpaceModel for latency calculation.
        **kwargs
            Keyword arguments for SearchSpacePytorchLatencyCalculator.
            Pass ``warmup_iterations`` to set number of warmup iterations before measuring, default 10.
            Pass ``run_iterations`` to set number of iterations for measuring, default 10.
            Pass ``get_base_samples`` to provide function that accepts ``inputs``, ``keyword_inputs``
            and returns samples number.
            Default implementation is based on the knowledge that ``inputs`` is Tuple of ``torch.Tensor``
            and number of samples doesn't depend on ``keyword_inputs``: ``inputs[0].shape[0]``.

        """
    def compute(self, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ...) -> SearchSpaceLatencyContainer: ...

class SearchSpacePytorchCpuLatencyCalculator(SearchSpacePytorchLatencyCalculator):
    """Search space CPU-time latency calculator."""
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None: ...

class SearchSpacePytorchCudaLatencyCalculator(SearchSpacePytorchLatencyCalculator):
    """Search space CUDA-time latency calculator."""
    def __init__(self, search_space: SearchSpaceModel, **kwargs) -> None: ...

def create_latency_calculator(latency_type: str, search_space: SearchSpaceModel, **kwargs) -> SearchSpaceLatencyCalculator:
    """
    Creates concrete `SearchSpaceLatencyCalculator` for latency calculation of specified type.

    Parameters
    ----------
    latency_type: str
        The type of latency that calculator will compute.
    search_space: SearchSpaceModel
        Search space for latency calculation.
    **kwargs
        Arbitrary keyword arguments for SearchSpaceLatencyCalculator.

    Returns
    -------
    SearchSpaceLatencyCalculator
        Concrete calculator for latency calculation of specified type.

    """
def initialize_latency(latency_type: str, search_space: SearchSpaceModel, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ..., **kwargs) -> SearchSpaceLatencyContainer:
    """
    Initializes latency of type ``latency_type`` in search space,
    latency_type should correspond to available :class:`.SearchSpaceLatencyCalculator`.
    To list available latency_type (calculators) use :func:`.available_calculators` function.

    Parameters
    ----------
    latency_type: str
        The type of latency to be initialized in search space.
    search_space: SearchSpaceModel
        Search space for latency calculation.
    inputs: Tuple
        Model input.
    keyword_inputs: Optional[Dict[str, Any]]
        Model keyword input arguments.
    **kwargs
        Arbitrary keyword arguments for :class:`.SearchSpaceLatencyCalculator`.

    Returns
    -------
    SearchSpaceLatencyContainer
        Calculated latency of search_space as :class:`.SearchSpaceLatencyContainer`.
        This container can be analyzed with the help of statistical tools from this module.

    """
def reset_latency(search_space: SearchSpaceModel) -> None:
    """
    Reset all latency parameters of search space.

    Parameters
    ----------
    search_space: SearchSpaceModel
        Search space which latency will be reset.

    """
def available_calculators() -> str:
    """
    Returns available search space calculators as string.

    Returns
    -------
    str
        List of available calculators.

    """
