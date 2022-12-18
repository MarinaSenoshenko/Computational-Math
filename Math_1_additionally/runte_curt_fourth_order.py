from params import *

ORDER = 4


class ApproximationWithFourthOrder(object):
    def __init__(self, h, n):
        self.h = h
        self.n = n
        self.y_array = [0] * (self.n + 1)
        self.x_array = [0] * (self.n + 1)

        self.k = [0] * ORDER
        self.alpha = [0] * ORDER

        self.fillAlpha()
        self.approximation()

    def fillAlpha(self):
        self.alpha[0] = 0
        self.alpha[1] = self.h / 2
        self.alpha[2] = self.h / 2
        self.alpha[3] = self.h

    def approximation(self):
        self.y_array[0] = 1 + sqrt(2)
        self.x_array[0] = 1

        for i in range(1, self.n + 1):
            self.x_array[i] = self.x_array[0] + i * self.h
            for j in range(ORDER):
                self.k[j] = G(self.x_array[i - 1] + self.alpha[j], self.y_array[i - 1] + self.alpha[j] * self.k[j - 1])
            self.y_array[i] = self.y_array[i - 1] + (self.h / 6) * (self.k[0] + 2 * self.k[1] + 2 * self.k[2] + self.k[3])
