from common.params import *


class DecisionInitializer(object):
    @staticmethod
    def initY(N, h, τ):
        y = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        for n in range(0, M + 1):
            for j in range(N + 1):
                if 4 >= x_0 + j * h - α * τ * n > 1:
                    y[n][j] = g(j * h + x_0 + α * τ * n)
        return y

    @staticmethod
    def Y(N, h, T):
        y = [0] * (N + 1)
        for j in range(N + 1):
            if 4 >= x_0 + j * h - α * T > 1:
                y[j] = g(j * h - α * T)
        return y


    @staticmethod
    def initX(N, h):
        x_grid = [0] * (N + 1)
        for i in range(N + 1):
            x_grid[i] = i * h + x_0
        return x_grid
