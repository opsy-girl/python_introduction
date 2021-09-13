import numpy as np
import math as mt
...
L1 norm is simply the sum of the absolute values of a vector values
...
def calculate_l1_norm(v):
  myNorm=0
  for normVal in v:
    myNorm += abs(normVal)
  return myNorm

abc=[2.0, -3.5, 5.1]
print(calculate_l1_norm(abc))



