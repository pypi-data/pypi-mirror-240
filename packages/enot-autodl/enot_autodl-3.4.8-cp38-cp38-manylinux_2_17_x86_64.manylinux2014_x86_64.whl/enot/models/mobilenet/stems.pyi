from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple

class MobileNetBaseStem(nn.Module):
    width_multiplier: Incomplete
    in_channels: Incomplete
    min_channels: Incomplete
    stem: Incomplete
    def __init__(self, *, activation: Optional[str] = ..., in_channels: int = ..., strides: Tuple[int, int] = ..., output_channels: Tuple[int, int] = ..., kernel_sizes: Tuple[int, int] = ..., width_multiplier: float = ..., min_channels: int = ...) -> None:
        """
        Makes first layers of network.

        Parameters
        ----------
        activation: str, optional
            Name for used activation function.

            This function must be registered in GLOBAL_ACTIVATION_FUNCTION_REGISTRY
            from enot.operations.operations_registry.

            If activation is None - there is no activation_function.

            Default value: 'relu6'
        in_channels:
            Number of channels in the input tensor. Default value: 3
        strides: tuple
            Strides for two convolution layers in stem. Default value: (2, 1)
        output_channels: tuple
            Number of channels in output tensors for two convolution layers in stem Default value: (32, 16)
        kernel_sizes: tuple
            Kernel sizes for two convolution layers in stem. Default value: (3, 3)
        width_multiplier:
            Adjusts number of channels in each layer by this amount.
        min_channels:
            Min_value parameter for _make_divisible function from original tf repo.
            It can be see here:
            https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py.

        """
    def forward(self, x): ...

MobileNetCifarStem: Incomplete
