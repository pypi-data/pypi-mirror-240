from enot.models import SearchSpaceModel
from pathlib import Path
from typing import List, Union

class SearchSpaceLatencyContainer:
    """Latency storage for :class:`.SearchSpaceModel`."""
    def __init__(self, latency_type: str, constant_latency: float, operations_latencies: List[List[float]]) -> None:
        """
        Parameters
        ----------
        latency_type: str
            Type of latency that container holds.
        constant_latency: float
            Constant latency of :class:`.SearchSpaceModel`.
        operations_latencies: List[List[float]]
            Latencies of all operations in NAS blocks.
        """
    @property
    def latency_type(self) -> str:
        """Returns latency type."""
    @property
    def constant_latency(self) -> float:
        """Returns constant latency of :class:`.SearchSpaceModel`."""
    @property
    def operations_latencies(self) -> List[List[float]]:
        """Returns latencies of all operations in Nas blocks."""
    @classmethod
    def load_from_file(cls, filename: Union[str, Path]) -> SearchSpaceLatencyContainer:
        """
        Creates :class:`.SearchSpaceLatencyContainer` from file.

        Parameters
        ----------
        filename: Union[str, Path]
            Filename of file with dumped :class:`.SearchSpaceLatencyContainer`.

        Returns
        -------
        SearchSpaceLatencyContainer

        """
    @classmethod
    def load_from_bytes(cls, data: bytes) -> SearchSpaceLatencyContainer:
        """
        Creates :class:`.SearchSpaceLatencyContainer` from bytes object.

        Parameters
        ----------
        data : bytes
            Bytes object from which container will be created.

        Returns
        -------
        SearchSpaceLatencyContainer

        """
    def save_to_file(self, filename: Union[str, Path]) -> None:
        """
        Saves latency container to file.

        Parameters
        ----------
        filename: Union[str, Path]
            Filename of file for dumping SearchSpaceLatencyContainer.

        """
    def save_to_bytes(self) -> bytes:
        """Dumps latency container to bytes object."""

def apply_latency_container(search_space: SearchSpaceModel, latency_container: SearchSpaceLatencyContainer) -> None:
    """
    Applies latencies from SearchSpaceLatencyContainer to the search space.

    Parameters
    ----------
    latency_container : SearchSpaceLatencyContainer
        Latency container to use for search space latency initialization.

    """
def extract_latency_container(search_space: SearchSpaceModel) -> SearchSpaceLatencyContainer:
    """
    Extracts search space latencies as a SearchSpaceLatencyContainer.

    Search space consists of two parts: dynamic (search blocks with their operations) and static (constant).
    SearchSpaceLatencyContainer represents latency information of a search space as latencies of static and dynamic
    parts.

    You can save and load SearchSpaceLatencyContainer to and from your hard drive, and apply them later again in
    your search space models.

    Returns
    -------
    SearchSpaceLatencyContainer
        Container with the necessary search space latency information.

    See Also
    --------
    SearchSpaceLatencyContainer : latency container documentation.
    enot.latency.search_space_latency_statistics : module with search space latency statistical information.

    """
