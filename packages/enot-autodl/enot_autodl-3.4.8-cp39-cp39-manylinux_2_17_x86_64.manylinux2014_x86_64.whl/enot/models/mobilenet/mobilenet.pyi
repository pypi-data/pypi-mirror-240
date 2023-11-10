import torch.nn as nn
from typing import Any, Dict, List

def build_mobilenet(search_ops: List[str], blocks_out_channels: List[int], blocks_count: List[int], blocks_stride: List[int], in_channels: int = ..., width_multiplier: float = ..., min_channels: int = ..., stem_params: Dict[str, Any] = ..., head_params: Dict[str, Any] = ..., init_weights_kn: bool = ..., dropout_rate: float = ..., num_classes: int = ...) -> nn.Sequential:
    """
    Build MobileNetV2 like architecture with search blocks instead of MIB. All search_ops will be in each search_block.

    Parameters
    ----------
    search_ops:
        List of string operations descriptions for search_blocks.
    blocks_out_channels: list
        List of output channels for each block in the network. Values for c from original MobileNetV2 paper.
    blocks_count: list
        List of number of block repeats. Values for n from original MobileNetV2 paper.
    blocks_stride: list
        List of strides for each block in the network. Values for s from original MobileNetV2 paper.
    in_channels: int
        Number of input channels for model.
        Default value: 3
    width_multiplier: float
        Adjusts number of channels in each layer by this amount.
        Default value: 1.0
    min_channels: int
        Min_value parameter for _make_divisible function from original tf repo.
        It can be see here:
        https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py.
        Default value: 8
    stem_params: dict, optional
        Additional parameters for enot.mobilenet.mobilenet.stems.MobileNetBaseStem constructor.
        In channels for network will be use as in_channels for stem.
    head_params: dict, optional
        Additional parameters for enot.mobilenet.mobilenet.stems.MobileNetBaseHead constructor.
        The last blocks_out_channels will be used as head_in_channels
    init_weights_kn: bool
        Flag for Kaiming He initialization. Default value: True
    dropout_rate: float
        Fraction of the neurons to drop. Default value: 0.0
    num_classes: int
        Number of predicted classes. Default value: 1000.

    """
def build_frozen_mobilenet(blocks_op_name: List[str], blocks_out_channels: List[int], blocks_count: List[int], blocks_stride: List[int], in_channels: int = ..., width_multiplier: float = ..., min_channels: int = ..., stem_params: Dict[str, Any] = ..., head_params: Dict[str, Any] = ..., dropout_rate: float = ..., num_classes: int = ..., init_weights_kn: bool = ...) -> nn.Sequential:
    """
    Construct MobileNetV2 like model with operations listed in blocks_op_name.

    Parameters
    ----------
    blocks_op_name:
        List of string operations descriptions for operations in the model.
    blocks_out_channels: list
        List of output channels for each block in the network. Values for c from original MobileNetV2 paper.
    blocks_count: list
        List of number of block repeats. Values for n from original MobileNetV2 paper.
    blocks_stride: list
        List of strides for each block in the network. Values for s from original MobileNetV2 paper.
    in_channels: int
        Number of input channels for model.
    width_multiplier: float
        Adjusts number of channels in each layer by this amount.
    min_channels: int
        Min_value parameter for _make_divisible function from original tf repo.
        It can be see here:
        https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py.
        Default value: 8
    stem_params: dict, optional
        Additional parameters for enot.mobilenet.mobilenet.stems.MobileNetBaseStem constructor.
        In channels for network will be use as in_channels for stem.
    head_params: dict, optional
        Additional parameters for enot.mobilenet.mobilenet.stems.MobileNetBaseHead constructor.
        The last blocks_out_channels will be used as head_in_channels
    init_weights_kn: bool
        Flag for Kaiming He initialization. Default value: True
    dropout_rate: float
        Fraction of the neurons to drop. Default value: 0.0
    num_classes: int
            Number of predicted classes. Default value: 1000.

    """
