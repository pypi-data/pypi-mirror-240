import numpy as np

from sz import Tensor


def rosenbrock(_x0, _x1):
    _y = 100 * (_x1 - _x0 ** 2) ** 2 + (_x0 - 1) ** 2
    return _y


x0 = Tensor(np.array(0.0))
x1 = Tensor(np.array(2.0))
lr = 0.001
iters = 50000

for i in range(iters):
    print(x0, x1)
    x0.clear_tensor()
    x1.clear_tensor()
    y = rosenbrock(x0, x1)
    y.backward()
    x0 -= lr * x0.grad
    x1 -= lr * x1.grad
"""
趋向于：Tensor(0.9999999993721514) Tensor(0.9999999987417905)
"""
