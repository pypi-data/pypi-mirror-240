from _typeshed import Incomplete
from torch import nn
from typing import Optional

class SearchableResNext(nn.Module):
    """
    ResNext block with group convolution.

    https://arxiv.org/pdf/1611.05431.pdf, fig. 3(c)

    """
    kernel_size: Incomplete
    cardinality: Incomplete
    expand_ratio: Incomplete
    stride: Incomplete
    padding: Incomplete
    in_channels: Incomplete
    out_channels: Incomplete
    hidden_channels: Incomplete
    block_operations: Incomplete
    use_skip_connection: Incomplete
    def __init__(self, in_channels: int, out_channels: int, hidden_channels: Optional[int] = ..., expand_ratio: Optional[float] = ..., kernel_size: int = ..., cardinality: int = ..., stride: int = ..., padding: Optional[int] = ..., activation: str = ..., use_skip_connection: bool = ...) -> None:
        """
        Parameters
        ----------
        in_channels: int
            Number of channels in the input tensor.
        out_channels: int
            Number of channels of output tensor.
        hidden_channels: int, optional
            Number of channels in the convolution inside ResnetBlock.
            Only one of hidden_channels and expand_ratio con be set.
            If both is None - hidden_channels=in_channels // 2.
        expand_ratio: float, optional
            Used for computing hidden_channels.
            hidden_channels = round(in_channels * expand_ratio).
        kernel_size: int
            Kernel size for middle group convolution in the block.
        cardinality: int
            Number of groups for middle group convolution.
        stride: int
            Stride of the depthwise convolution. Default value: 1
        padding: int, optional
            Padding added to both sides of the input. Default value: None (that means 'same')
        activation: str, optional
            Name for used activation function.

            This function must be registered in GLOBAL_ACTIVATION_FUNCTION_REGISTRY
            from enot.operations.operations_registry.

            If activation is None - there is no activation_function.

            Default value: 'relu'
        """
    def forward(self, x): ...
