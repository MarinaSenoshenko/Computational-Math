def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

eps = 0.001
ans = 1000000000000

if b ** 2 - 3 * a * c > 0:
    x_1 = -(2 * b - (4 * (b ** 2 - 3 * a * c)) ** 0.5) / 6 * a
    x_2 = -(2 * b + (4 * (b ** 2 - 3 * a * c)) ** 0.5) / 6 * a
    extr = 2

    if f(x_1) * f(x_2) < 0:
        root = 3
    elif f(x_1) * f(x_2) == 0:
        root = 2
    else:
        root = 1
else:
    root = 1
    if b ** 2 - 3 * a * c < 0:
        extr = 0
        x_1 = x_2 = 1000000000
    extr = 1
    x_1 = x_2 = -2 * b / 6 * a

print("{0} roots".format(root))

if (x_1 > x_2):
    tmp = x_1
    x_1 = x_2
    x_2 = tmp


a_n = -10000000000
b_n = x_1

for i in range(0, 3):
    while abs(b_n - a_n) > eps:
        res = (a_n + b_n) / 2
        if f(b_n) * f(res) == 0:
            if f(b_n) == 0:
                res = b_n
            break
        elif f(a_n) * f(res) == 0:
            if f(a_n) == 0:
                res = a_n
            break
        elif f(a_n) * f(res) < 0:
            b_n = res
        elif f(b_n) * f(res) < 0:
            a_n = res
        else:
            break

    if abs(b_n - a_n) <= eps:
        print("in range [{0},{1}]".format(a_n, b_n))
        root -= 1
    elif f(res) == 0:
        if (ans != res):
            print(res)
            root -= 1
            ans = res

    if root == 0:
        break

    if i == 0:
        if extr > 1:
            a_n = x_1
            b_n = x_2
        else:
            b_n = 1000000000.0
    if i == 1:
        a_n = x_2
        b_n = 1000000000.0







