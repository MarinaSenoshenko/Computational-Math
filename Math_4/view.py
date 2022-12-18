import matplotlib.pyplot as plt
from approximator import f

MANY_POINTS = 1000000


class CauchyTaskVisualizer(object):
    def __init__(self, x_array, y_array, a):
        self.a = a
        self.x_array = x_array
        self.y_array = y_array

    @staticmethod
    def markLabels():
        plt.xlabel("x label")
        plt.ylabel("y label")
        plt.legend(['Approximation graphic'], loc=3)

    def showApproximationGraphic(self):
        plt.plot(self.x_array, self.y_array)
        self.markLabels()
        self.printOriginalFunctionGraphic()
        plt.show()

    def printOriginalFunctionGraphic(self):
        arr_x = [0] * (MANY_POINTS + 1)
        arr_y = [0] * (MANY_POINTS + 1)
        for j in range(MANY_POINTS + 1):
            arr_x[j] = -self.a + j * 2 * self.a / MANY_POINTS
            arr_y[j] = f(arr_x[j])
        plt.plot(arr_x, arr_y)
