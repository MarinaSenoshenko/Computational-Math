import math
import time

PI = 3.14159265358979323846
ONE_ROOT = 2.9716938707138902397986


def f(x):
    return x - l * math.cos(x)


def dif_f(x):
    return 1 + l * math.sin(x)


def countOffset(a, b):
    while abs(a - b) > eps:
        res = (a + b) / 2

        if dif_f(res) * dif_f(b) < 0:
            a = res
        elif dif_f(a) * dif_f(res) < 0:
            b = res
        else:
            break
    return a


def iter_step(x_1, x_2):
    return x_2 - (((x_2 - x_1) / (f(x_2) - f(x_1))) * f(x_2))


def secantMethod(x_0, x_1):
    x_2 = 0
    while abs(x_1 - x_0) > eps:
        x_2 = iter_step(x_0, x_1)
        x_0, x_1 = x_1, x_2
    return x_2


def printAnswer(step, ind, root_container):
    if step > 0:
        if ind:
            print("List of {0} more then zero roots: {1} ".format(ind, root_container))
        else:
            print("{0} roots more then zero ".format(ind))
    else:
        if ind:
            print("List of {0} less then zero roots: {1} ".format(ind, root_container))
        else:
            print("{0} roots less then zero ".format(ind))


def findRoot(step, root_counter, offset):
    x = math.asin(-1 / l)
    x_a = x
    x_b = x + step + offset
    root_container = []
    ind = 0

    while f(x_a) * f(x_b) < 0:
        root = secantMethod(x_a, x_b)
        root_container.append(root)
        root_counter += 1
        ind += 1

        if ind % 2 == 1:
            x_a, x_b, x = x + step + offset, x + 2 * step, x + step
        else:
            x_a, x_b, x = x + step, x + 2 * step + offset, x + step

    printAnswer(step, ind, root_container)
    return root_counter


l = float(input("Choose the parameter 'l' for equation x = lcosx\nl = "))
eps = 0.000001
start = time.perf_counter()

if -ONE_ROOT < l < ONE_ROOT:
    print("{0} root: {1}".format(1, secantMethod(-l, l)))

else:
    x0 = math.asin(-1 / l) + PI
    x1 = countOffset(x0 - 1, x0 + 1)
    dif = x1 - x0
    print("Total root count: {0}".format(findRoot(-PI, findRoot(PI, 0, dif), dif)))

print("Time roots counting: {0} sec".format(time.perf_counter() - start))