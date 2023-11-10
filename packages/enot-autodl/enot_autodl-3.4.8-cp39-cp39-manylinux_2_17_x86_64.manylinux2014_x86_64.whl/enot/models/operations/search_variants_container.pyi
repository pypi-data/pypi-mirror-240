import torch.nn as nn
from _typeshed import Incomplete
from enot.models.operations.search_operations_container import SearchableOperationsContainer as SearchableOperationsContainer
from enot.utils.common import iterate_by_submodules as iterate_by_submodules
from typing import Any, Iterable, Optional

class SearchVariantsContainer(nn.Module):
    """
    Container class which keeps searchable operations.

    If you want to perform Neural Architecture Search, your model should
    have at least one `SearchVariantsContainer`.

    User can add any modules as search operations into this container.
    Currently, we are not allowing nested search variant containers.

    Notes
    -----
    This module keeps choice options as nn.ModuleList in `search_variants`
    attribute. After search space initialization, this attribute is
    replaced with Search container.

    """
    search_variants: Incomplete
    call_operation: Incomplete
    def __init__(self, search_variants: Iterable[nn.Module], default_operation_index: int = ..., **kwargs) -> None:
        """
        Parameters
        ----------
        search_variants : iterable with torch.nn.Modules
            Iterable object, which contains search variants of current
            graph node.
        default_operation_index: int or None, optional
            Index of operation which will be used as a default
            operation in forward before SearchVariantsContainer is
            wrapped with SearchSpaceModel. Default value is None, which
            ensures that ValueError is raised in the case of attempt
            to call SearchVariantsContainer before wrapping.

        """
    def set_default_operation(self, operation_index: Optional[int]) -> None: ...
    def forward(self, *args, **kwargs) -> Any: ...
