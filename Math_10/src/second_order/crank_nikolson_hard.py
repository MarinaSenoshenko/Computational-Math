from common.params import *
from order_set import setOrder


class Approximator(object):
    def __init__(self, h, N, tao):
        self.h = h
        self.N = N
        self.tao = tao
        self.tao_cur = tao
        self.order = 2
        self.methodName = 'Crank-Nicholson non-linear'
        self.u = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        self.u_prev = [0] * (N + 1)
        self.u_cur = [0] * (N + 1)

        self.count()

    def count(self):
        self.u[0] = initU_0(self.N, self.h)
        setOrder(self)

        for n in range(1, M + 1):
            self.tao_cur = correctTao(self.N, n, self.u, self.h)
            self.tridiagonalMatrixRunning(n)


    def condition(self):
        for i in range(self.N + 1):
            if abs(self.u_cur[i] - self.u_prev[i]) > 0.01:
                return 1
        return 0

    def tridiagonalMatrixRunning(self, n):
        a = [0] * (self.N + 1)
        c = [0] * (self.N + 1)
        d = [0] * (self.N + 1)

        for j in range(self.N + 1):
            self.u_prev[j] = 0
            self.u_cur[j] = 1

        while self.condition():
            for j in range(self.N + 1):
                self.u_prev[j] = self.u_cur[j]

            ksi = [0] * (self.N + 1)
            nu = [0] * (self.N + 1)
            for j in range(self.N + 1):
                if j != 0:
                    a[j] = -(self.u_prev[j - 1]) * (self.tao_cur / (4 * self.h))
                if j != self.N:
                    c[j] = self.u_prev[j + 1] * (self.tao_cur / (4 * self.h))
                d[j] = self.u[n - 1][j]

            for j in range(self.N + 1):
                if j == 0:
                    ksi[0] -= c[0]
                    nu[0] = d[0]
                else:
                    if j != self.N:
                        ksi[j] -= c[j] / (1 + a[j] * ksi[j - 1])
                    nu[j] -= (a[j] * nu[j - 1] - d[j]) / (1 + a[j] * ksi[j - 1])

            self.u_cur[self.N] = nu[self.N]
            for j in range(self.N, 0, -1):
                self.u_cur[j - 1] = (ksi[j - 1] * self.u_cur[j] + nu[j - 1])


        for j in range(2, self.N - 2):
            self.u[n][j] = self.u_cur[j]


