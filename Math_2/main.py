from threading import Thread

E = 2.71828
max_allowed_degree = 40


def f(x):
    return E**x - a - x


def iter_step(x_1, x_2):
    dif_x = x_2 - x_1
    dif_f = f(x_2) - f(x_1)
    return x_2 - ((dif_x / dif_f) * f(x_2))


def algorithm(x_0, x_1, x_2):
    while abs(x_1 - x_0) > eps:
        x_2 = iter_step(x_0, x_1)
        x_0, x_1 = x_1, x_2
    print("root: {0}, ".format(x_2))


def findFirstRoot():
    algorithm(- a - 0.5, - a + 0.5, 0)


a = float(input("Choose the parameter 'a' for equation e^x = x + a\na = "))
eps = 0.0000001

if a > 1:
    print("this equation has 2 roots:")

    thread = Thread(target=findFirstRoot)
    thread.start()
    thread.join()

    x_a = max_allowed_degree
    x_b = x_c = 0
    while abs(x_a - x_b) > 1:
        res = (x_a + x_b) / 2

        if f(res) * f(x_b) < 0:
            x_a = res
        elif f(x_a) * f(res) < 0:
            x_b = res
    algorithm(x_a, x_b, x_c)


elif a == 1:
    print("this equation has 1 root:\n0")
else:
    print("this equation has 0 roots")






