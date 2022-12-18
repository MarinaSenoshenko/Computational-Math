import math

E = 2.7182818284

def f(x):
    #return math.log(x + 1, E)
    return pow(E, x) * math.cos(x)


def f_2(x):
    #return - 1 / pow(x + 1, 2)
    return -2 * pow(E, x) * math.sin(x)


def f_4(x):
    #return -6 / pow(x + 1, 4)
    return -4 * pow(E, x) * math.cos(x)
