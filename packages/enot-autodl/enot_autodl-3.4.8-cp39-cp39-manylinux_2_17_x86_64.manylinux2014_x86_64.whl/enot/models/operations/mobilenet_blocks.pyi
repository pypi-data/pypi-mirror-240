from _typeshed import Incomplete
from torch import nn
from typing import Optional

class SearchableMobileInvertedBottleneck(nn.Module):
    """
    Searchable block from MobileNetV2.

    https://arxiv.org/pdf/1801.04381.pdf

    """
    in_channels: Incomplete
    out_channels: Incomplete
    kernel_size: Incomplete
    stride: Incomplete
    expand_ratio: Incomplete
    padding: Incomplete
    dw_channels: Incomplete
    affine: Incomplete
    track: Incomplete
    activation_function_name: Incomplete
    activation_function: Incomplete
    expand_op: Incomplete
    depthwise_op: Incomplete
    squeeze_op: Incomplete
    use_skip_connection: Incomplete
    def __init__(self, in_channels: int, out_channels: int, dw_channels: Optional[int] = ..., expand_ratio: Optional[float] = ..., kernel_size: int = ..., stride: int = ..., padding: Optional[int] = ..., affine: bool = ..., track: bool = ..., activation: Optional[str] = ..., use_skip_connection: bool = ...) -> None:
        """
        Parameters
        ----------
        in_channels: int
            Number of channels in the input tensor.
        out_channels: int
            Number of channels of output tensor.
        dw_channels: int, optional
            Number of channels in depthwise convolution.
            Only one of dw_channels and expand_ratio con be set.
            If both is None there is no expand operation and only depthwise and squeeze blocks will be compute.
        expand_ratio: float, optional
            Used for computing dw_channels.

            dw_channels = round(in_channels * expand_ratio).
        kernel_size: int
            Size of the convolving kernel in the depthwise convolution. Default value: 3
        stride: int
            Stride of the depthwise convolution. Default value: 1
        padding: int, optional
            Padding added to both sides of the input. Default value: None (that means 'same')
        affine: bool
            Flag for using affine in all BatchNorm-s of MIB.
        track: bool
            Flag for using track_running_stats in all BatchNorm-s of MIB.
        activation: str, optional
            Name for used activation function.

            This function must be registered in GLOBAL_ACTIVATION_FUNCTION_REGISTRY
            from enot.operations.operations_registry.

            If activation is None - there is no activation_function.

            Default value: 'relu6'
        use_skip_connection: bool
            Add skip connection (y+=x) if this flag is True
            and output produced by convolution has the same shape as input.
            Default value: True
        """
    def forward(self, x): ...
