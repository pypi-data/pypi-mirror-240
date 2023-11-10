import torch
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import Any, Dict

ms_to_us: Incomplete
s_to_ms: Incomplete
s_to_us: Incomplete

class TimeEvent(metaclass=ABCMeta):
    """Synchronization markers that can be used to monitor the device’s progress,
    to accurately measure timing."""
    def __init__(self) -> None: ...
    @property
    def name(self) -> str: ...
    def measure_time() -> Any: ...
    measure_time: Incomplete
    def measure_time_delta(start: Any, end: Any) -> float: ...
    measure_time_delta: Incomplete
    def record_start(self) -> None: ...
    def record_end(self) -> None: ...
    def evaluate(self) -> float: ...
    @abstractmethod
    def to_chrome_trace_event(self, ref_time: Any) -> Dict:
        """
        Exports `TimeEvent` to Chrome Trace event format.

        Parameters
        ----------
        ref_time
            Is used as reference time (point) for current event.

        Returns
        -------
        Dict
            Chrome Trace representation of `TimeEvent`.

        """

class CPUTimeEvent(TimeEvent):
    @staticmethod
    def measure_time() -> float: ...
    @staticmethod
    def measure_time_delta(start: float, end: float) -> float: ...
    def to_chrome_trace_event(self, ref_time) -> Dict: ...

class CUDATimeEvent(TimeEvent):
    @staticmethod
    def measure_time() -> torch.cuda.Event: ...
    @staticmethod
    def measure_time_delta(start: torch.cuda.Event, end: torch.cuda.Event) -> float: ...
    def to_chrome_trace_event(self, ref_time: torch.cuda.Event) -> Dict: ...
