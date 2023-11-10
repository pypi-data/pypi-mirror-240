import torch.nn as nn
import torch
from _typeshed import Incomplete
from typing import List, Optional, Union

class ConvBNActivation(nn.Module):
    """Default Conv+BN+Act block, but with modules names like in YoloV5."""
    conv: Incomplete
    bn: Incomplete
    act: Incomplete
    def __init__(self, conv: torch.nn.Conv2d, bn: torch.nn.BatchNorm2d, act: Optional[torch.nn.Module] = ...) -> None:
        """
        Parameters
        ----------
        conv : torch.nn.Conv2d
            Convolution module.
        bn : torch.nn.BatchNorm2d
            Batchnorm module.
        act : torch.nn.Module, optional
            Activation function.

        """
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward_fuse(self, x): ...

class Bottleneck(nn.Module):
    """Default Bottleneck block, but with modules names like in YoloV5."""
    cv1: Incomplete
    cv2: Incomplete
    add: Incomplete
    def __init__(self, conv1: ConvBNActivation, conv2: ConvBNActivation, skip: bool) -> None:
        """
        Parameters
        ----------
        conv1 : ConvBNActivation
            First convolution in bottleneck.
        conv2 : ConvBNActivation
            Second convolution in bottleneck.
        skip : bool
            Add skip connection or not.

        """
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class BottleNecksSequence(nn.Module):
    """
    Stack of Bottleneck blocks.

    We need this to make leaf module to find C3 and Conv+C3 blocks.
    Also store expansion and depth for pruning.

    """
    body: Incomplete
    def __init__(self, bottlenecks: Union[nn.Sequential, List[Bottleneck]]) -> None:
        """
        Parameters
        ----------
        bottlenecks : torch.nn.Sequential or list of Bottleneck
            List or Sequential module with stacked Bottleneck blocks.

        """
    @property
    def bottlenecks_count(self) -> int:
        """
        Number of bottlenecks following each other.

        Returns
        -------
        int

        """
    @property
    def width_expansion(self) -> float:
        """
        Adjusts number of inner channels in each bottleneck by this amount.

        Returns
        -------
        float

        """
    @property
    def args(self): ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class C3(nn.Module):
    """C3 block from Yolov5."""
    cv1: Incomplete
    cv2: Incomplete
    cv3: Incomplete
    bottle: Incomplete
    def __init__(self, cv1: ConvBNActivation, cv2: ConvBNActivation, cv3: ConvBNActivation, bottlenecks: BottleNecksSequence) -> None:
        """
        Parameters
        ----------
        cv1 : ConvBNActivation
            The first input module with conv2d, batch norm2d and activation. Output goes to bottlenecks.
        cv2 : ConvBNActivation
            The second input module with conv2d, batch norm2d and activation.
        cv3 : ConvBNActivation
            conv2d, batch norm2d and activation module. Input – concated outputs of bottlenecks and cv2.
        bottlenecks : BottleNecksSequence
            Sequence of bottlenecks.

        """
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class RepVGGBlock(nn.Module):
    """RepVGGBlock is a basic rep-style block, including training and deploy status
    This code is based on https://github.com/DingXiaoH/RepVGG/blob/main/repvgg.py."""
    nonlinearity: Incomplete
    rbr_identity: Incomplete
    rbr_dense: Incomplete
    rbr_1x1: Incomplete
    def __init__(self, skip_bn: nn.BatchNorm2d, rbr_dense: ConvBNActivation, rbr_1x1: ConvBNActivation, activation: nn.Module) -> None: ...
    def forward(self, inputs: torch.Tensor) -> torch.Tensor: ...

class BepC3(nn.Module):
    """Beer-mug RepC3 Block."""
    cv1: Incomplete
    cv2: Incomplete
    cv3: Incomplete
    concat: Incomplete
    m: Incomplete
    def __init__(self, cv1: nn.Module, cv2: nn.Module, cv3: nn.Module, m: nn.Module, concat: bool = ...) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...

class BottleRepVgg(nn.Module):
    cv1: Incomplete
    cv2: Incomplete
    def __init__(self, cv1: nn.Module, cv2: nn.Module) -> None: ...
    def forward(self, x: torch.Tensor) -> torch.Tensor: ...
