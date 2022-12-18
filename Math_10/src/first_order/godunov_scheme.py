from common.params import *

class Approximator(object):
    def __init__(self, h, N, tao):
        self.h = h
        self.N = N
        self.tao = tao
        self.methodName = 'Godunov-scheme linear'
        self.u = [[0 for _ in range(self.N + 1)] for _ in range(M + 1)]
        self.count()

    def count(self):
        self.u[0] = initU_0(self.N, self.h)
        for n in range(1, M + 1):
            for j in range(self.N + 1):
                self.u[n][j] = r * self.u[n - 1][j - 1] + (1 - r) * self.u[n - 1][j]
