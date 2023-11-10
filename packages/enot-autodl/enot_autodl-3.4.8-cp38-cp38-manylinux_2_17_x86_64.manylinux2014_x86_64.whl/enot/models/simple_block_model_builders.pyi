import torch.nn as nn
from typing import List

def make_divisible(v: int, divisor: int, min_value: int = ...) -> int:
    """
    Function is taken from the original tf repo.
    It ensures that all layers have a channel number that is divisible by 8
    It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py.

    Parameters
    ----------
    v: int
    divisor: int
    min_value: int

    """
def build_simple_block_model(in_channels: int, search_ops: List[str], blocks_out_channels: List[int], blocks_count: List[int], blocks_stride: List[int], width_multiplier: float = ..., min_channels: int = ..., stem: nn.Module = ..., head: nn.Module = ..., init_weights_kn: bool = ...) -> nn.Sequential:
    """
    Build sequential block model. This model is compatible for SearchSpaceModel(model).

    Parameters
    ----------
    in_channels: int
        Number of input channels for model.
    search_ops:
        List of string operations descriptions for search_blocks.
    blocks_out_channels: list
        List of output channels for each block in the network.
    blocks_count: list
        List of number of block repeats.
    blocks_stride: list
        List of strides for each block in the network.
    width_multiplier: float
        Adjusts number of channels in each layer by this amount.
        Default value: 1.0
    min_channels: int
        Min_value parameter for _make_divisible function from original tf repo.
        It can be see here:
        https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py.
        Default value: 8
    stem: torch.nn.Module
        First layers of the network.
    head: torch.nn.Module
        Last layers of the network
    init_weights_kn: bool
        Flag for Kaiming He initialization. Default value: True

    Returns
    -------
        torch.nn.Sequential
            Sequence of stem (if passed), blocks, head(if passed)

    """
def build_frozen_simple_block_model(in_channels: int, blocks_op_name: List[str], blocks_out_channels: List[int], blocks_count: List[int], blocks_stride: List[int], width_multiplier: float = ..., min_channels: int = ..., stem: nn.Module = ..., head: nn.Module = ..., init_weights_kn: bool = ...) -> nn.Sequential:
    """
    Build simple sequential block model. It use for creating searched model using string descriptions of operations.

    Parameters
    ----------
    in_channels: int
        Number of input channels for model.
    blocks_op_name:
        List of string operations descriptions for operations in the model.
    blocks_out_channels: list
        List of output channels for each block in the network.
    blocks_count: list
        List of number of block repeats.
    blocks_stride: list
        List of strides for each block in the network.
    width_multiplier: float
        Adjusts number of channels in each layer by this amount.
        Default value: 1.0
    min_channels: int
        Min_value parameter for _make_divisible function from original tf repo.
        It can be see here:
        https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py.
        Default value: 8
    stem: torch.nn.Module
        First layers of the network.
    head: torch.nn.Module
        Last layers of the network
    init_weights_kn: bool
        Flag for Kaiming He initialization. Default value: True

    Returns
    -------
        torch.nn.Sequential
            Sequence of stem (if passed), blocks, head(if passed)

    """
