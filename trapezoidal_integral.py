from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

import math
math.pi
N=100
a=0
b=1/2*math.pi
def f(x):
    return sin(x)
h=(b-a)/N

S=0
for k in range(1, N+1):
    S+=1/2*h*(f(a+k*h)+f(a+(k-1)*h))
print(S)


