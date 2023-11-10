from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

class SearchableConv2d(nn.Module):
    """Sequence of (conv2d, [activation_function], batch_norm) layers."""
    in_channels: Incomplete
    out_channels: Incomplete
    stride: Incomplete
    kernel_size: Incomplete
    padding: Incomplete
    conv2d: Incomplete
    activation_function: Incomplete
    batch_norm: Incomplete
    use_skip_connection: Incomplete
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = ..., stride: Union[int, Tuple[int, int]] = ..., padding: Optional[int] = ..., activation: Optional[str] = ..., use_skip_connection: bool = ...) -> None:
        """
        Parameters
        ----------
        in_channels : int
            Number of channels in the input tensor.
        out_channels : int
            Number of channels produced by the convolution.
        kernel_size : int
            Size of the convolving kernel. Default value: 3
        stride : Union[int, Tuple[int, int]]
            Stride of the convolution. Default value: 1
        padding : int, optional
            Padding added to both sides of the input. Default value: None (that means 'same')
        activation : str, optional
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
    def forward(self, x):
        """
        Perform (conv2d, [activation_function if not None], batch_norm) sequentially.

        Parameters
        ----------
        x: torch.Tensor

        Returns
        -------
        output: torch.Tensor
            Tensor with results of computation.

        """

class SearchableFuseableSkipConv(SearchableConv2d):
    """
    SearchableConv2d without activation function, and with kernel_size=1.

    Used for matching input and output channels of search blocks.

    """
    def __init__(self, in_channels: int, out_channels: int, stride: Union[int, Tuple[int, int]] = ..., use_skip_connection: bool = ...) -> None: ...
