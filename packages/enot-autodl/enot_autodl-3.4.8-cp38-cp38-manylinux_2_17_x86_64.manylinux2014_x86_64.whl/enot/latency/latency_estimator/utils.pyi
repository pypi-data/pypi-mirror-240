from enot.latency.latency_estimator.item_latency_record import ItemLatencyRecord as ItemLatencyRecord
from enot.latency.latency_estimator.time_event import CPUTimeEvent as CPUTimeEvent, CUDATimeEvent as CUDATimeEvent, TimeEvent as TimeEvent
from typing import Any, Dict, List, Optional, Tuple

def get_time_event(device: str) -> TimeEvent: ...
def get_total_samples(records: List[ItemLatencyRecord]) -> float: ...
def get_total_time(records: List[ItemLatencyRecord]) -> float: ...
def default_get_base_samples(inputs: Tuple[Any, ...], keyword_inputs: Optional[Dict[str, Any]] = ...):
    """
    Returns number of samples in `inputs` (`keyword_inputs`) in the case of `inputs` is Tuple of `torch.Tensor``
    and number of samples doesn't depend on keyword_inputs.

    The implementation is:
    >>> return inputs[0].shape[0]

    """
