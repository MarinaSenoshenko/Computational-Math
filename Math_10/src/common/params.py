from math import *

M = 400
A = 6
α = 0.5
r = 0.5
π = 3.1415926535897932384626433832795
hInitial = 0.2
x_0 = -1
controlTime = 2

def g(x):
    return sin((π * (x - 1)) / 3)

def f(x):
    return pow(x, 2) / 2


def initU_0(N, h):
    u_0 = [0] * (N + 1)
    for j in range(0, N + 1):
        # if 4 > j * h >= 1:
        #     u_0[j] = g(j * h)

        if 0 >= j * h + x_0:
            u_0[j] = 2
        else:
            u_0[j] = 1

    return u_0


def initD(j, n, u, N):
    if j == 0:
        return 0.25 * r * (u[n - 1][j + 1]) + u[n - 1][j]
    if j == N:
        return 0.25 * r * (u[n - 1][j - 1]) + u[n - 1][j]
    return 0.25 * r * (u[n - 1][j - 1] - u[n - 1][j + 1]) + u[n - 1][j]


def correctTao(N, n, u, h):
    max = 0
    for i in range(N + 1):
        if abs(pow(u[n - 1][i], 2) / 2) > max:
            max = abs(f(u[n - 1][i]))
    return 0.2 * h / max


def rungeCheck(approximator, u1, u2, compareParams):
    maxOrder = 0
    for i in range(approximator.N + 1):
        localOrder = abs((u1[i] - u2[2 * i]) / (pow(2, approximator.order) - 1))
        if localOrder > maxOrder:
            maxOrder = localOrder
    print('for k = {0}, {1}, correctness = {2}'.format(approximator.order, compareParams, maxOrder))
