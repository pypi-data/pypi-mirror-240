import sz
from sz import CUDA, Tensor, Config
from sz.functions import max_backward_shape
from sz.functions.bf import Function
from sz.functions.ft0 import reshape, broadcast_to

"""
函数类型5：其它函数
最大值[max]、最小值[min]、限定数组上下界[clip]、准确度[accuracy]、退出[dropout]、批量[batch_norm]、嵌入ID[embed_id]
"""


def max(x, axis=None, keepdims=False):
    return Max(axis, keepdims)(x)


def min(x, axis=None, keepdims=False):
    return Min(axis, keepdims)(x)


def clip(x, x_min, x_max):
    return Clip(x_min, x_max)(x)


def accuracy(y, t):
    """
    不可微
    """
    y, t = (y if isinstance(y, Tensor) else Tensor(y)), (t if isinstance(t, Tensor) else Tensor(t))
    pred = y.data.argmax(axis=1).reshape(t.shape)
    result = (pred == t.data)
    acc = result.average()
    return sz.to_tensor(acc)


def dropout(x, dropout_ratio=0.5):
    if not isinstance(x, Tensor):
        x = Tensor(x)
    if Config.TRAIN:
        xp = CUDA.to_gpu()
        mask = xp.random.rand(*x.shape) > dropout_ratio
        scale = xp.array(1.0 - dropout_ratio).astype(x.dtype)
        y = x * mask / scale
        return y
    else:
        return x


def batch_norm(x, gamma, beta, mean, var, decay=0.9, eps=2e-5):
    return BatchNorm(mean, var, decay, eps)(x, gamma, beta)


def embed_id(x, W):
    return W[x]


class Max(Function):
    """
    max
    """

    def __init__(self, axis=None, keepdims=False):
        """
        初始化
        :param axis: 参数axis
        :param keepdims: 参数keepdims
        """
        self.axis = axis
        self.keepdims = keepdims

    def forward(self, x):
        """
        max的正向传播
        :param x: 参数x
        :return: max函数的计算结果
        """
        y = x.max(axis=self.axis, keepdims=self.keepdims)
        return y

    def backward(self, gy):
        """
        max的反向传播
        :param gy: 导数值
        :return: max函数的的反向传播的值
        """
        x = self.inputs[0]
        y = self.outputs[0]()  # 弱引用
        shape = max_backward_shape(x, self.axis)
        gy = reshape(gy, shape)
        y = reshape(y, shape)
        cond = (x.data == y.data)
        gy = broadcast_to(gy, cond.shape)
        return gy * cond


class Min(Max):
    """
    min
    """

    def forward(self, x):
        """
        min的正向传播
        :param x: 参数x
        :return: min函数的计算结果
        """
        y = x.min(axis=self.axis, keepdims=self.keepdims)
        return y


class Clip(Function):
    """
    clip
    """

    def __init__(self, x_min, x_max):
        """
        初始化
        :param x_min: 最小值
        :param x_max: 最大值
        """
        self.x_min = x_min
        self.x_max = x_max

    def forward(self, x):
        """
        clip的正向传播
        :param x: 参数x
        :return: clip函数的计算结果
        """
        xp = CUDA.to_gpu()
        y = xp.clip(x, self.x_min, self.x_max)
        return y

    def backward(self, gy):
        """
        clip的反向传播
        :param gy: 导数值
        :return: clip函数的的反向传播的值
        """
        x, = self.inputs
        mask = (x.data >= self.x_min) * (x.data <= self.x_max)
        gx = gy * mask
        return gx


class BatchNorm(Function):
    """
    batch_norm
    """

    def __init__(self, mean, var, decay, eps):
        """
        初始化
        :param mean: 参数mean
        :param var: 参数var
        :param decay: 参数decay
        :param eps: 参数eps
        """
        self.avg_mean = mean
        self.avg_var = var
        self.decay = decay
        self.eps = eps
        self.inv_std = None

    def forward(self, x, gamma, beta):
        """
        batch_norm的正向传播
        :param x: 参数x
        :param gamma: 参数gamma
        :param beta: 参数beta
        :return: batch_norm函数的计算结果
        """
        assert x.ndim == 2 or x.ndim == 4

        x_ndim = x.ndim
        if x_ndim == 4:
            N, C, H, W = x.shape
            # (N, C, H, W) -> (N * H * W, C)
            x = x.transpose(0, 2, 3, 1).reshape(-1, C)

        xp = CUDA.to_gpu()

        if Config.TRAIN:
            mean = x.mean(axis=0)
            var = x.var(axis=0)
            inv_std = 1 / xp.sqrt(var + self.eps)
            xc = (x - mean) * inv_std

            m = x.size // gamma.size
            s = m - 1. if m - 1. > 1. else 1.
            adjust = m / s  # unbiased estimation
            self.avg_mean *= self.decay
            self.avg_mean += (1 - self.decay) * mean
            self.avg_var *= self.decay
            self.avg_var += (1 - self.decay) * adjust * var
            self.inv_std = inv_std
        else:
            inv_std = 1 / xp.sqrt(self.avg_var + self.eps)
            xc = (x - self.avg_mean) * inv_std
        y = gamma * xc + beta

        if x_ndim == 4:
            # (N * H * W, C) -> (N, C, H, W)
            y = y.reshape(N, H, W, C).transpose(0, 3, 1, 2)
        return y

    def backward(self, gy):
        """
        batch_norm的反向传播
        :param gy: 导数值
        :return: batch_norm函数的的反向传播的值
        """
        gy_ndim = gy.ndim
        if gy_ndim == 4:
            N, C, H, W = gy.shape
            gy = gy.transpose(0, 2, 3, 1).reshape(-1, C)

        x, gamma, beta = self.inputs
        batch_size = len(gy)

        if x.ndim == 4:
            N, C, H, W = x.shape
            x = x.transpose(0, 2, 3, 1).reshape(-1, C)
        mean = x.sum(axis=0) / batch_size
        xc = (x - mean) * self.inv_std

        gbeta = sum(gy, axis=0)
        ggamma = sum(xc * gy, axis=0)
        gx = gy - gbeta / batch_size - xc * ggamma / batch_size
        gx *= gamma * self.inv_std

        if gy_ndim == 4:
            gx = gx.reshape(N, H, W, C).transpose(0, 3, 1, 2)
        return gx, ggamma, gbeta
