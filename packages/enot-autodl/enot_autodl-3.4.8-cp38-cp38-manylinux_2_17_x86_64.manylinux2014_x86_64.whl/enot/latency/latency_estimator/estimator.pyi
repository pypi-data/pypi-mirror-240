import torch
from pathlib import Path
from typing import List, Optional, Tuple, Union

class PytorchLatencyEstimator:
    """
    Measures latency (time in milliseconds) of module or search space.
    PytorchLatencyEstimator supports ``CPU`` and ``CUDA`` devices.

    Examples
    --------
    >>> estimator = PytorchLatencyEstimator(
    ...     model=search_space,
    ...     latency_type='cpu',
    ... )
    >>> n_base_samples = 8
    >>> inputs = torch.ones(n_base_samples, 3, 224, 224)
    >>> estimator.record_item(n_base_samples=n_base_samples)
    >>> sampler = PermutationSampler(search_space)
    >>> for arch in sampler:
    >>>     search_space.sample(arch)
    >>>     search_space(inputs)
    >>> constant_latency, operations_latencies = estimator.get_latencies()
    """
    def __init__(self, model: torch.nn.Module, latency_type: str, **options) -> None:
        """
        PytorchLatencyEstimator supports two types of latency (`latency_type` parameter):

        - ``cpu``
        - ``cuda``

        Parameters
        ----------
        model : torch.nn.Module
            Model or search space that will be measured.
        latency_type : str
            Type of latency for measuring.
        **options
            To trace all modules pass `trace_all_modules=True` to options.

        """
    def record_item(self, n_base_samples: Union[float, int] = ...) -> None:
        """
        Add item to record.

        See Also
        --------
        Example in class description.

        Parameters
        ----------
        n_base_samples : Union[float, int]
            Number of samples to record.

        """
    def get_latencies(self, return_sample_time: bool = ...) -> Tuple[float, Optional[List[List[float]]]]:
        """
        For ordinary models returns measured latency.

        For SearchSpace models returned latency will be consists of two parts:
         - latency of constant (static) part of model
         - latencies of operations packed into lists

        Parameters
        ----------
        return_sample_time : bool
            Whether to return model latency for single sample or all samples.

        Returns
        -------
        Tuple[float, Optional[List[List[float]]]]:
            Returns measured latency for ordinary models.
            For SearchSpaces, constant latency is supplemented by latencies of operations.

        """
    def export_chrome_trace(self, filename: Union[str, Path]) -> None:
        """
        Exports all measurements to file with Chrome(ium) tracing format:
        https://www.chromium.org/developers/how-tos/trace-event-profiling-tool.

        Use `export_chrome_trace` with `trace_all_modules=True` to refine trace graph.

        Parameters
        ----------
        filename : Union[str, Path]
            File to export.

        """
