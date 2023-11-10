from enot.optimize import PretrainOptimizer, SearchOptimizer
from torch.optim import Optimizer
from typing import Union

OptimizerClass = Union[Optimizer, PretrainOptimizer, SearchOptimizer]

def log_begin(logger, optimizer: OptimizerClass) -> None:
    """
    Appends initial information about statistics to tensorboard.

    Parameters
    ----------
    logger : SummaryWriter or None
        SummaryWriter to use for tensorboard logging. If None, then no
        logging is made.
    optimizer : Optimizer or PretrainOptimizer or SearchOptimizer
        Optimizer instance to log pretrain or search related statistics.

    """
def log_step(logger, optimizer: OptimizerClass, step: int) -> None:
    """
    Appends per-step information about statistics to tensorboard.

    Parameters
    ----------
    logger : SummaryWriter or None
        SummaryWriter to use for tensorboard logging. If None, then no
        logging is made.
    optimizer : Optimizer or PretrainOptimizer or SearchOptimizer
        Optimizer instance to log pretrain or search related statistics.
    step : int
        Current pretrain step.

    """
def log_train_end(logger, optimizer: OptimizerClass, epoch: int) -> None:
    """
    Appends training information about statistics to tensorboard.

    Parameters
    ----------
    logger : SummaryWriter or None
        SummaryWriter to use for tensorboard logging. If None, then no
        logging is made.
    optimizer : Optimizer or PretrainOptimizer or SearchOptimizer
        Optimizer instance to log pretrain or search related statistics.
    epoch : int
        Current pretrain epoch.

    """
def log_validation_end(logger, optimizer: OptimizerClass, epoch: int) -> None:
    """
    Appends validation information about statistics to tensorboard.

    Parameters
    ----------
    logger : SummaryWriter or None
        SummaryWriter to use for tensorboard logging. If None, then no
        logging is made.
    optimizer : Optimizer or PretrainOptimizer or SearchOptimizer
        Optimizer instance to log pretrain or search related statistics.
    epoch : int
        Current pretrain epoch.

    """
