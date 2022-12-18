import pandas as pd

E = 2.7182818284590452353602874713527


def f(x):
    return -pow(E, -x)


class CauchyTaskApproximator(object):
    def __init__(self, a, n, h):
        self.a = a
        self.n = n
        self.h = h
        self.middle = n // 2

        self.x_array = [0] * (n + 1)
        self.y_array = [0] * (n + 1)
        self.discrepancy_array = [0] * (n + 1)

    def count(self, y, sgn):
        return (1 - sgn * self.h) * y

    def approximation(self, sgn):
        y_cur = -1
        x_cur = 0
        for i in range(1, self.middle + 1):
            y_cur = self.count(y_cur, sgn)
            x_cur += sgn * self.h
            self.x_array[self.middle + sgn * i] = x_cur
            self.y_array[self.middle + sgn * i] = y_cur

    def countApproximation(self):
        self.y_array[self.middle] = -1
        self.x_array[self.middle] = 0

        self.approximation(-1)
        self.approximation(1)

    def findDiscrepancy(self):
        sgn = 1
        for i in range(self.n + 1):
            if i == self.middle:
                sgn = -1
            self.discrepancy_array[i] = -sgn * self.h * f(self.x_array[i]) * self.x_array[i] / 2

    def printResult(self):
        pd.set_option('display.max_rows', None)
        print(pd.DataFrame({
            'x': self.x_array,
            'y': self.y_array,
            'discrepancy': self.discrepancy_array}))
