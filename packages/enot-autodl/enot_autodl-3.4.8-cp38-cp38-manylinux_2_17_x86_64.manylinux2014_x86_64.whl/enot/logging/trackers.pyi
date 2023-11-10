from typing import Any

class RunningMeanLogger:
    """Tracks running mean value."""
    def __init__(self, momentum: float = ...) -> None: ...
    @property
    def running_value(self) -> Any: ...
