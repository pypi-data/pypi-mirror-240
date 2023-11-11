import sz
from sz import CUDA, Tensor, Config

"""
函数类型5：其它函数2
准确度[accuracy]、退出[dropout]、嵌入ID[embed_id]
"""


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


def embed_id(x, W):
    return W[x]
