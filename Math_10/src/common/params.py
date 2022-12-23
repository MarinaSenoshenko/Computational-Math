from math import *

M = 800
A = 8
α = 0.5
r = 0.25
π = 3.1415926535897932384626433832795
hInitial = 0.1
x_0 = 0
controlTime = 4

def g(x):
    return sin((π * (x - 1)) / 3)

def f(x):
    return pow(x, 2) / 2


def initU_0(N, h):
    u_0 = [0] * (N + 1)
    for j in range(0, N + 1):
        if 4 > j * h >= 1:
            u_0[j] = g(j * h)

        # if 0 >= j * h + x_0:
        #     u_0[j] = 2
        # else:
        #     u_0[j] = 1

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
        if abs(u[n - 1][i]) > max:
            max = abs(u[n - 1][i])
    return 0.5 * h / max
