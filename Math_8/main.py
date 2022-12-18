from func1 import f, f_2, f_4


def trapezoidMethod(a, b, n):
    s = 0
    h = (b - a) / n
    x = a
    for i in range(1, n + 1):
        s += (f(x + h) + f(x)) * h / 2
        x += h
    return s


def threeEightMethod(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        x = a + h * i
        if i % 3 == 0:
            s += 2 * f(x)
        else:
            s += 3 * f(x)

    s *= (3 / 8) * h
    return s


def errorRateTrapezoidMethod(a, b, n):
    x = a
    max_from_f_2 = 0
    for i in range(n + 1):
        if abs(f_2(x)) > max_from_f_2:
            max_from_f_2 = abs(f_2(x))
        x += (b - a) / n

    return pow(b - a, 3) * max_from_f_2 / (12 * pow(n, 2))


def errorRateThreeEightMethod(a, b, n):
    x = a
    max_from_f_4 = 0
    for i in range(n + 1):
        if abs(f_4(x)) > max_from_f_4:
            max_from_f_4 = abs(f_4(x))
        x += (b - a) / n

    return pow(b - a, 5) * max_from_f_4 / (80 * pow(n, 4))


def printResult(n):
    print("trapezoid method integral for n = {0}: {1}, |R(f)| <= {2}".format(n, trapezoidMethod(0, 2, n), errorRateTrapezoidMethod(0, 2, n)))
    print("three eight method integral for n = {0}: {1}, |R(f)| <= {2}\n".format(n, threeEightMethod(0, 2, n), errorRateThreeEightMethod(0, 2, n)))


printResult(3)
printResult(9)
printResult(210)
printResult(2100)
