import numpy as np

from sz.accelerate.cuda import CUDA
from sz.core.config import Config
from sz.core.tensor import Tensor
from sz.core.numericaldiff import NumericalDiff
from sz.ds.queue import PriorityQueue
from sz.ds.stack import Stack
from sz.functions.ft0 import sum_to, SumTo, broadcast_to, BroadcastTo
from sz.functions.ft1 import setup_tensor, power, Power
from sz.functions.ft3 import exp, Exp

setup_tensor()


def is_tensor(obj):
    """
    判断对象是不是Tensor对象
    :param obj: 要判断的对象
    :return: True：是Tensor对象；False：不是Tensor对象
    """
    return isinstance(obj, Tensor)


def as_nparray(obj):
    """
    将对象转化为numpy的数组
    为什么需要转化：
    x = np.array(0.5)
    y = np.array([0.5])
    x = x + 1
    y = y + 1
    print(np.isscalar(x))  # True
    print(np.isscalar(y))  # False
    :param obj: 要转化的对象
    :return: 转化后的对象
    """
    if np.isscalar(obj):
        return np.array(obj)
    return obj


def to_tensor(obj):
    """
    将对象转化为Tensor对象
    :param obj: 要转化的对象
    :return: 转化后的对象
    """
    obj = as_nparray(obj)
    if not is_tensor(obj):
        obj = Tensor(obj)
    return obj
