import math
import matplotlib.pyplot as plt
import numpy as np

MANY_POINTS = 1000000


def f(x_root):
    return x_root + math.log(x_root, 5)


def lagP(x_root, count):
    step = (b - a) / count
    z = 0
    for i in range(0, count + 1):
        p = 1.0
        for k in range(0, count + 1):
            if k != i:
                x_k = a + k * step
                x_i = a + i * step
                p *= (x_root - x_k) / (x_i - x_k)
        y_i = f(a + i * step)
        z += y_i * p
    return z


def checkInputParameters():
    test = 1
    if a <= 0:
        test = 0
        print("Incorrect 'a' parameter. It should be more then zero")
    if point > b or point < a:
        test = 0
        print("Incorrect number of check point. It should be in range [a, b]")
    if n <= 0:
        test = 0
        print("Incorrect count of knots. It should be more than zero")
    return test


def printRes(count):
    arr_x = []
    arr_p = []
    step = (b - a) / count
    print("/*******************************************/")
    for i in range(0, count + 1):
        x_i = a + i * step
        y_i = lagP(a + i * step, count)
        arr_x.append(x_i)
        arr_p.append(y_i)
        print("x_{0} = {1}, P(x_{2}) = {3}".format(i, x_i, i, y_i))

    plt.plot(arr_x, arr_p)
    print("Error rate for point {0} with {1} knots: {2}".format(point, count + 1, abs(lagP(point, count) - f(point))))


def printOriginalFunctionGraphic():
    arr_x = [0] * MANY_POINTS
    arr_y = [0] * MANY_POINTS
    for i in range(MANY_POINTS):
        arr_x[i] = a + i * (b - a) / MANY_POINTS
        arr_y[i] = f(arr_x[i])
    plt.plot(arr_x, arr_y)


def markLabels():
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.text(0, b, "green graphic: f(x) = x + lg(x.5)")
    plt.text(0, b - b / 10, "blue graphic: L(x) for {0} knots".format(n))
    plt.text(0, b - b / 5, "orange graphic: L(x) for {0} knots".format(2 * n))


a, b, = map(float, input("Your function: x + lg(x.5)\nEnter point 'a' and 'b' for [a, b]: ").split())
n = int(input("Enter count of points: "))
point = float(input("Enter check point: "))

if checkInputParameters():
    printRes(n - 1)
    printRes(2 * n - 1)

    x = np.linspace(a, b, 100)
    printOriginalFunctionGraphic()
    markLabels()

    plt.show()
