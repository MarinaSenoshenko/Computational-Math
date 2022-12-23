from common.params import *
from controller import Controller


u = initU_0(int((A + abs(x_0)) / 10e-4), 10e-4)

max = 0
for i in range(int((A + abs(x_0)) / 10e-4) + 1):
    if abs(u[i]) > max:
        max = abs(u[i])
print(max)


Controller(max)


