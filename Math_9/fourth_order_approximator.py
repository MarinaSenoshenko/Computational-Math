import numpy as np
import pandas as pd

E = 2.7182818284590452353602874713527
CHECK_POINT1 = 20
CHECK_POINT2 = 10
ORDER = 4


def diff_5(x):
    return pow(E, x) * np.cos(x) + pow(E, x) * np.sin(x)


def g(x):
    return pow(E, x) * np.sin(x)


class Approximator(object):
    def __init__(self, n, h):
        self.n = n
        self.h = h

        self.x_array = [0] * (n + 1)
        self.y_array = [0] * (n + 1)
        self.discrepancy_array = [0] * (n + 1)

    def count(self, x0, x1, x2, y0):
        return y0 + self.h * (g(x2) + g(x0) + 4 * g(x1)) / 3

    def countApproximationResult(self):
        self.y_array[0] = 1
        self.x_array[0] = 0

        # self.y_array[1] = pow(E, self.h) * (np.sin(self.h) - np.cos(self.h)) / 2 + 1.5
        self.x_array[1] = self.h

        for i in range(2, self.n + 1):
            self.x_array[i] = i * self.h
            self.y_array[i] = self.count(self.x_array[i - 2], self.x_array[i - 1], self.x_array[i], self.y_array[i - 2])
            if i == 2:
                self.y_array[1] = self.y_array[2] - (self.h / 12) * (
                            8 * g(self.x_array[2]) + 5 * g(self.x_array[1]) - g(self.x_array[3]))
            if i == CHECK_POINT1:
                print((self.y_array[CHECK_POINT1] - self.y_array[CHECK_POINT2]) / (pow(2, ORDER) - 1))

    def findDiscrepancy(self):
        for i in range(2, self.n + 1):
            self.discrepancy_array[i] = -pow(self.h, 4) * diff_5(self.x_array[i]) / 180

    def printResult(self):
        pd.set_option('display.max_rows', None)
        print(pd.DataFrame({
            'x': self.x_array,
            'y': self.y_array,
            'discrepancy': self.discrepancy_array}))
