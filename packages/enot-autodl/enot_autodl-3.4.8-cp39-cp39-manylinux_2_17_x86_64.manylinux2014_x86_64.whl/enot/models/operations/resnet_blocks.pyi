from _typeshed import Incomplete
from torch import nn
from typing import Optional

class SearchableResNetD(nn.Module):
    """
    D type of ResNet block.

    https://arxiv.org/pdf/1603.05027.pdf fig. 4(d)

    """
    in_channels: Incomplete
    out_channels: Incomplete
    expand_ratio: Incomplete
    expand_kernel_size: Incomplete
    squeeze_kernel_size: Incomplete
    stride: Incomplete
    padding: Incomplete
    block_operations: Incomplete
    use_skip_connection: Incomplete
    def __init__(self, in_channels: int, out_channels: int, hidden_channels: Optional[int] = ..., expand_ratio: Optional[float] = ..., squeeze_kernel_size: int = ..., expand_kernel_size: int = ..., stride: int = ..., padding: Optional[int] = ..., activation: str = ..., use_skip_connection: bool = ...) -> None:
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
        squeeze_kernel_size: int
            Kernel size for squeeze convolution from in_channels to hidden_channels.
        expand_kernel_size: int
            Kernel size for expand convolution from hidden_channels to out_channels.
        stride: int
            Stride of the depthwise convolution. Default value: 1
        padding: int, optional
            Padding added to both sides of the input. Default value: None (that means 'same')
        activation: str, optional
            Name for used activation function.

            This function must be registered in GLOBAL_ACTIVATION_FUNCTION_REGISTRY
            from enot.operations.operations_registry.

            If activation is None - there is no activation_function

            Default value: 'relu'
        use_skip_connection: bool
            Add skip connection (y+=x) if this flag is True, in_channels==out_channels and stride==1.
            Default value: True
        """
    def forward(self, x): ...

class SearchableResNetE(nn.Module):
    """
    E type of ResNet block.

    https://arxiv.org/pdf/1603.05027.pdf, fig. 4(e)

    """
    in_channels: Incomplete
    out_channels: Incomplete
    expand_ratio: Incomplete
    expand_kernel_size: Incomplete
    squeeze_kernel_size: Incomplete
    stride: Incomplete
    padding: Incomplete
    block_operations: Incomplete
    use_skip_connection: Incomplete
    def __init__(self, in_channels: int, out_channels: int, hidden_channels: Optional[int] = ..., expand_ratio: Optional[float] = ..., squeeze_kernel_size: int = ..., expand_kernel_size: int = ..., stride: int = ..., padding: Optional[int] = ..., activation: str = ..., use_skip_connection: bool = ...) -> None:
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
        squeeze_kernel_size: int
            Kernel size for squeeze convolution from in_channels to hidden_channels.
        expand_kernel_size: int
            Kernel size for expand convolution from hidden_channels to out_channels.
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
        use_skip_connection: bool
            Add skip connection (y+=x) if this flag is True
            and output produced by convolution has the same shape as input.
            Default value: True
        """
    def forward(self, x): ...
