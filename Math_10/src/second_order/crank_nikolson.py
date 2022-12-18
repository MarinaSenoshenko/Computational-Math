from common.params import *


class Approximator(object):
    def __init__(self, h, N, tao):
        self.h = h
        self.N = N
        self.tao = tao
        self.methodName = 'Crank-Nicholson linear'
        self.u = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        self.count()

    def count(self):
        self.u[0] = initU_0(self.N, self.h)
        for n in range(1, M + 1):
            self.tridiagonalMatrixRunning(n)

    def tridiagonalMatrixRunning(self, n):
        d = [0] * (self.N + 1)
        ksi = [0] * (self.N + 1)
        nu = [0] * (self.N + 1)

        for j in range(self.N + 1):
            d[j] = initD(j, n, self.u, self.N)

        for j in range(self.N + 1):
            if j == 0:
                ksi[0] -= 0.25 * r
                nu[0] = d[0]
            else:
                if j != self.N:
                    ksi[j] -= 0.25 * r /  (1 - 0.25 * r * ksi[j - 1])
                nu[j] -= (-0.25 * r * nu[j - 1] - d[j]) / (1 - 0.25 * r * ksi[j - 1])

        self.u[n][self.N] = nu[self.N]
        for j in range(self.N, 0, -1):
            self.u[n][j - 1] = (ksi[j - 1] * self.u[n][j] + nu[j - 1])