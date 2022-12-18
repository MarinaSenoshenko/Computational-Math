from math import sqrt
import pandas as pd

N = 4
A = 2
MANY_POINTS = 1000000
E = 2.7182818284590452353602874713527

def G(x, u):
    return (2 * pow(x, 2) + 3 * x * u - pow(u, 2)) / (x * u - pow(x, 2))

def printResult(approximator1, approximator2):
    y_array = [0] * (N + 1)
    diff2 = [0] * (N + 1)
    diff4 = [0] * (N + 1)
    for i in range(N + 1):
        y_array[i] = approximator1.x_array[i] * (sqrt(2) + 1)
        diff2[i] = y_array[i] - approximator1.y_array[i]
        diff4[i] = y_array[i] - approximator2.y_array[i]

    pd.set_option('display.max_rows', None)
    print(pd.DataFrame({
        'x': approximator1.x_array,
        'k = 2': approximator1.y_array,
        'k = 4': approximator2.y_array,
        'diff 2': diff2,
        'diff 4': diff4,
        'y': y_array}))

def rungeCheck(approximator1, approximator2, order):
    maxOrder = 0
    for i in range(N + 1):
        localOrder = abs((approximator1.y_array[i] - approximator2.y_array[2 * i])) / (pow(2, order) - 1)
        if localOrder > maxOrder:
            maxOrder = localOrder
    print('k = {0}, correctness = {1}'.format(order, maxOrder))
