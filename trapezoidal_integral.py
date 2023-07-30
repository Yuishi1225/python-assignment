from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

def calculus(f,b=1,a=0,N=100):
    h=(b-a)/N
    S=0
    for k in range(1, N+1):
        S+=1/2*h*(f(a+k*h)+f(a+(k-1)*h))
    return S

def n(x):
    return 4/(1+x**2)

def y(x):
    return (math.pi**(1/2))*(math.exp(-x**2))

#(1)
result1 =calculus(sin, b=math.pi/2, a=0, N=50)
print(result1)
#(2)
result2 =calculus(n,a=0, b=1 , N=100)
print(result2)
#(3)

result3= calculus(y, a=-100, b=100, N=1000)
print(result3)







