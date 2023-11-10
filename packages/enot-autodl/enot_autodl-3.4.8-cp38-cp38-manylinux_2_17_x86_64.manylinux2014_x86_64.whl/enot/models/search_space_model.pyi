import torch
from _typeshed import Incomplete
from enot.core import SearchSpace
from enot.models.operations.search_variants_container import SearchVariantsContainer
from torch import nn
from typing import Any, List, Optional, Tuple, Union

class SearchSpaceModel(SearchSpace):
    """
    Search space model class.

    This class takes a regular PyTorch model (with SearchVariantsContainer in it) and moves it to the search space.
    SearchSpaceModel is responsible for all necessary preparations to move regular model to the search space and to
    extract the best model from the already pre-trained search space.

    """
    original_model: Incomplete
    def __init__(self, original_model: nn.Module, **kwargs) -> None:
        """
        Parameters
        ----------
        original_model : torch.nn.Module
            Model with search variants containers, which will be moved to search space.
        kwargs
            Experimental options (should be ignored by user).

        """
    @property
    def latency_type(self) -> Optional[str]:
        """
        Selected latency type.

        Returns
        -------
        str or None
            Name of the latency type or None if latency is not initialized.

        """
    @property
    def constant_latency(self) -> float:
        """
        Search space constant latency value.

        Returns
        -------
        float
            The total latency of search space constant modules (which are outside of any SearchVariantsContainer).

        """
    @property
    def forward_latency(self) -> torch.Tensor:
        """
        Returns current forward latency of search space's current selected architecture.

        Returns
        -------
        torch.Tensor
            Latency of the search space sub-network stored in tensor with a single float value.

        """
    @property
    def output_distribution_optimization_enabled(self) -> bool:
        """
        Output distribution optimization status.

        Returns
        -------
        bool
            True if output distribution optimization is enabled, and False otherwise.

        """
    @property
    def search_variants_containers(self) -> List[SearchVariantsContainer]:
        """
        Finds all SearchVariantsContainer in the original model.

        Returns
        -------
        list with SearchVariantsContainer
            List with all SearchVariantsContainer of the original model.

        """
    def get_network_by_indexes(self, selected_op_index: Union[Tuple[int, ...], List[int]]) -> nn.Module:
        """
        Extracts regular model with the fixed architecture.

        Parameters
        ----------
        selected_op_index : tuple with int or list with int
            Indices of the selected architecture. i-th list value is an i-th SearchVariantsContainer operation index.

        Returns
        -------
        torch.nn.Module
            Model with the fixed architecture.

        """
    def get_network_with_best_arch(self) -> nn.Module:
        """
        Extracts model with the best architecture.

        Returns
        -------
        torch.nn.Module
            Model with the best architecture.

        """
    def initialize_output_distribution_optimization(self, *sample_input_args, **sample_input_kwargs) -> None:
        '''
        Initializes "output distribution" optimization.

        Output distribution optimization is highly recommended for "pretrain" step.

        Parameters
        ----------
        sample_input_args
            Input arguments used in initialization forward pass.
        sample_input_kwargs
            Input keyword arguments used in initialization forward pass.

        Raises
        ------
        RuntimeError
            If output distribution optimization is already enabled.

        '''
    def forward(self, *args, **kwargs) -> Any:
        """
        Executes search space forward pass.

        Parameters
        ----------
        args
            Network input arguments. They are passed directly to the original model.
        kwargs
            Network input keyword arguments. They are passed directly to the original model.

        Returns
        -------
        Any
            User network execution result.

        """
