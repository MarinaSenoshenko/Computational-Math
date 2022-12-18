import matplotlib.pyplot as plt
from common.params import *
from common.exact_decision import DecisionInitializer


class Visualizer(object):
    def __init__(self, approximator1, approximator2, approximator3, approximator4):
        self.approximator1 = approximator1
        self.approximator2 = approximator2
        self.approximator3 = approximator3
        self.approximator4 = approximator4

        self.methodName = approximator1.methodName

        self.u1 = approximator1.u
        self.u2 = approximator2.u
        self.u3 = approximator3.u
        self.u4 = approximator4.u

        self.x_grid1 = DecisionInitializer.initX(approximator1.N, approximator1.h)
        self.x_grid2 = DecisionInitializer.initX(approximator2.N, approximator2.h)
        self.x_grid3 = DecisionInitializer.initX(approximator3.N, approximator3.h)
        self.x_grid4 = DecisionInitializer.initX(approximator4.N, approximator4.h)

    def showGraphic(self):
        plt.xlabel("x label")
        plt.ylabel("u label")
        u1 = u2 = u3 = u4 = 0
        for i in range(M + 1):
            if self.approximator1.tao * i == controlTime:
                plt.plot(self.x_grid1, self.u1[i], label='step h')
                u1 = self.u1[i]
            if self.approximator2.tao * i == controlTime:
                plt.plot(self.x_grid2, self.u2[i], label='step h/2')
                u2 = self.u2[i]
            if self.approximator3.tao * i == controlTime:
                plt.plot(self.x_grid3, self.u3[i], label='step h/4')
                u3 = self.u3[i]
            if self.approximator4.tao * i == controlTime:
                plt.plot(self.x_grid4, self.u4[i], label='step h/8')
                u4 = self.u4[i]
                # plt.plot(x_grid, y, label='original func')

        rungeCheck(self.approximator1, u1, u2, 'h and h / 2')
        rungeCheck(self.approximator2, u2, u3, 'h / 2 and h / 4')
        rungeCheck(self.approximator3, u3, u4, 'h / 4 and h / 8')

        plt.legend()
        plt.title(self.methodName + ' compare' + ' with h = {0}'.format(self.approximator1.h))
        plt.show()
