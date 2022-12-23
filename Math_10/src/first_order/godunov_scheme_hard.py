from common.params import *

class Approximator(object):
    def __init__(self, h, N, tao):
        if r > 1:
            raise ValueError('Incorrect r')
        self.h = h
        self.N = N
        self.tao = tao
        self.tao_cur = tao
        self.order = 1
        self.methodName = 'Godunov-scheme non-linear'
        self.u = [[0 for _ in range(self.N + 1)] for _ in range(M + 1)]
        self.count()

    def count(self):
        self.u[0] = initU_0(self.N, self.h)
        for j in range(1, M + 1):
            self.u[j][0] = self.u[0][0]

        for j in range(1, M + 1):
            self.u[j][self.N] = self.u[0][self.N]

        for n in range(1, M + 1):
            self.tao_cur = correctTao(self.N, n, self.u, self.h)
            for j in range(1, self.N):
                self.u[n][j] = self.u[n - 1][j] - (self.tao_cur / self.h) * (f(self.u[n - 1][j]) - f(self.u[n - 1][j - 1]))
