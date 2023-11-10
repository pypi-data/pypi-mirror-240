import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from torch import nn
from typing import Any, Dict, List, Optional, Tuple, Type

LCALC_REGISTRY: Incomplete

class LatencyCalculator(ABC, metaclass=abc.ABCMeta):
    """Base class for latency calculators."""
    @abstractmethod
    def calculate(self, model: nn.Module, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ..., ignore_modules: Optional[List[Type[nn.Module]]] = ..., **options) -> float:
        """
        Calculates model latency.

        Parameters
        ----------
        model : torch.nn.Module
            Model for latency calculation.
        inputs : Tuple[torch.Tensor, ...]
            Model input.
        ignore_modules : Optional[List[Type[nn.Module]]]
            List of types of modules that will be ignored in latency calculation.

        Returns
        -------
        float
            Model latency.

        """

class MacCalculator(LatencyCalculator):
    """Wrapper for third-party MAC calculators."""
    def calculate(self, model: nn.Module, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ..., ignore_modules: Optional[List[Type[nn.Module]]] = ..., **options) -> float:
        """
        Calculates number of Multiply-Accumulate operations in model.

        Parameters
        ----------
        model : torch.nn.Module
            Model for MAC operations calculation.
        inputs : Tuple[torch.Tensor, ...]
            Model inputs stored in tuple.
        keyword_inputs : Optional[Dict[str, Any]]
            Model keyword inputs.
        ignore_modules : Optional[List[Type[nn.Module]]]
            List of types of modules, that will be ignored in MAC calculation.

        Returns
        -------
        float:
            Number of MAC operations in model (in millions).

        """

class MacCalculatorThop(MacCalculator):
    """Wrapper for https://github.com/Lyken17/pytorch-OpCounter."""
    def calculate(self, model: nn.Module, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ..., ignore_modules: Optional[List[Type[nn.Module]]] = ..., **options) -> float: ...

class MacCalculatorPthflops(MacCalculator):
    """Wrapper for https://github.com/1adrianb/pytorch-estimate-flops."""
    def calculate(self, model: nn.Module, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ..., ignore_modules: Optional[List[Type[nn.Module]]] = ..., **options) -> float: ...

class MacCalculatorFvcore(MacCalculator):
    """Wrapper for https://github.com/facebookresearch/fvcore."""
    def __init__(self, **kwargs) -> None: ...
    def calculate(self, model: nn.Module, inputs: Tuple, keyword_inputs: Optional[Dict[str, Any]] = ..., ignore_modules: Optional[List[Type[nn.Module]]] = ..., **options) -> float: ...
