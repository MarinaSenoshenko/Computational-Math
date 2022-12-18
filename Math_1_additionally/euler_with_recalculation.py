from params import *


class ApproximationWithSecondOrder(object):
    def __init__(self, h, n):
        self.h = h
        self.n = n
        self.y_array = [0] * (n + 1)
        self.x_array = [0] * (n + 1)

        self.approximation()

    def approximation(self):
        self.y_array[0] = 1 + sqrt(2)
        self.x_array[0] = 1

        for i in range(1, self.n + 1):
            self.x_array[i] = self.x_array[0] + i * self.h
            g1 = G(self.x_array[i - 1], self.y_array[i - 1])
            g2 = G(self.x_array[i - 1] + self.h, self.y_array[i - 1] + self.h * g1)
            self.y_array[i] = self.y_array[i - 1] + (self.h / 2) * (g1 + g2)
