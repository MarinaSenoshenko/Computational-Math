from params import *
import matplotlib.pyplot as plt


def root(x):
    return x * (sqrt(2) + 1)


class Visualizer(object):
    def __init__(self, x_array, y_array1, y_array2):
        self.x_array = x_array
        self.y_array1 = y_array1
        self.y_array2 = y_array2

    def showApproximationGraphic(self):
        plt.plot(self.x_array, self.y_array1, 'k o')  # blue - k = 2
        plt.plot(self.x_array, self.y_array2)  # orange - k = 4
        self.printOriginalFunctionGraphic()  # green - answer
        plt.show()

    @staticmethod
    def printOriginalFunctionGraphic():
        arr_x = [0] * (MANY_POINTS + 1)
        arr_y = [0] * (MANY_POINTS + 1)
        for j in range(MANY_POINTS + 1):
            arr_x[j] = j * (1 / MANY_POINTS) + 1
            arr_y[j] = root(arr_x[j])
        plt.plot(arr_x, arr_y)
