import torch
from _typeshed import Incomplete
from torch import nn

class MobileNetBaseHead(nn.Module):
    last_channels: Incomplete
    bottleneck_channels: Incomplete
    width_multiplier: Incomplete
    num_classes: Incomplete
    head: Incomplete
    def __init__(self, bottleneck_channels: int, *, activation: str = ..., last_channels: int = ..., dropout_rate: float = ..., num_classes: int = ..., width_multiplier: float = ...) -> None:
        """
        Builds last layers of network.

        Parameters
        ----------
        bottleneck_channels:
            Number of input channels for convolution before FC layer.
        activation: str, optional
            Name for used activation function.

            This function must be registered in GLOBAL_ACTIVATION_FUNCTION_REGISTRY
            from enot.operations.operations_registry.

            If activation is None - there is no activation_function.

            Default value: 'relu6'
        last_channels:
            Number of output channels for convolution before FC layer. Default value: 1280
        dropout_rate:
             Default value: 0
        num_classes:
            Number of predicted classes. Default value: 1000.
        width_multiplier:
            Adjusts number of channels in each layer (conv2d and fc) by this amount.

        """
    def forward(self, x): ...

class ArcfaceHead(nn.Linear):
    radius: Incomplete
    angle_margin: Incomplete
    cos_margin: Incomplete
    angle_scale: Incomplete
    num_classes: Incomplete
    vectorizer: Incomplete
    def __init__(self, bottleneck_channels: int, *, radius: float = ..., angle_margin: float = ..., cos_margin: float = ..., angle_scale: float = ..., last_channels: int = ..., num_classes: int = ...) -> None:
        """
        Arcface layer with parameters from original paper.
        .. _original paper:
        https://arxiv.org/pdf/1801.07698.pdf.

        Parameters
        ----------
        bottleneck_channels: int
            Number of input channels for convolution before FC layer.
        radius: float
            Radius of sphere for embeddings. Default value: 64.0
        angle_margin: float
            Value for m2 parameter from original paper. Default value: 0.5
        cos_margin: float
            Value for m3 parameter from original paper. Default value: 0.0
        angle_scale: float
            Value for m1 parameter from original paper. Default value: 1.0
        last_channels: int
            Number of output channels for convolution before FC layer. Default value: 1280
        num_classes: int
            Number of predicted classes. Default value: 1000.

        """
    def forward(self, inputs: torch.Tensor, labels: torch.Tensor = ...) -> torch.Tensor: ...
    @staticmethod
    def corrected_cos(inputs: torch.Tensor) -> torch.Tensor: ...
