from common.params import *


class DecisionInitializer(object):

    @staticmethod
    def Y(N, h, num):
        y = [0] * (N + 1)
        for j in range(N + 1):
            if num == 1:
                if 4 >= x_0 + j * h - α * controlTime > 1:
                    y[j] = g(j * h - α * controlTime)
            if num == 2:
                if 0 >= x_0 + j * h - α * controlTime:
                    y[j] = 2
                else:
                    y[j] = 1
        return y

    @staticmethod
    def initX(N, h):
        x_grid = [0] * (N + 1)
        for i in range(N + 1):
            x_grid[i] = i * h + x_0
        return x_grid


