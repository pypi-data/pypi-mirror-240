import numpy as np

from sz.core.tensor import Tensor
from sz.functions.ft2 import sin


x = Tensor(np.array(1.0))
y = sin(x)
y.backward()
for i in range(3):
    gx = x.grad
    x.clear_tensor()
    gx.backward()
    print(x.grad.data)
"""
e
a
b
c
d
-0.8414709848078965
-0.5403023058681398
0.8414709848078965
"""
