import torch.nn as nn
import torch
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

class ConvBN(nn.Module):
    conv: Incomplete
    bn: Incomplete
    activation: Incomplete
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = ..., stride: int = ..., padding: Optional[int] = ..., bn: bool = ..., groups: int = ..., affine: bool = ..., track: bool = ..., activation: Optional[str] = ...) -> None: ...
    def forward(self, x): ...

class DepthwiseConvBN(ConvBN):
    def __init__(self, in_channels: int, kernel_size: int = ..., stride: int = ..., padding: Optional[int] = ..., bn: bool = ..., affine: bool = ..., track: bool = ..., activation: Optional[str] = ...) -> None: ...

class SkipConnection(nn.Module):
    operation: Incomplete
    downsample: Incomplete
    def __init__(self, operation: nn.Module, downsample: Optional[nn.Module] = ...) -> None: ...
    def forward(self, x: torch.Tensor): ...

def calculate_hidden_channels(in_channels, hidden_channels, expand_ratio): ...
def same_padding(kernel_size: Union[int, Tuple[int, ...]], dilation: Union[int, Tuple[int, ...]] = ...) -> Union[int, Tuple[int, ...]]:
    """
    Implement padding 'SAME'.

    This is only here to avoid code de-synchronization.

    """

class Swish(nn.Module):
    sigmoid: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...
