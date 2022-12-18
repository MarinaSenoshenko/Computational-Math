import time

CONVERT_TO_MILLSEC = 1000


def LUDecompozition(a, b, n):
    print("LUDecompozition method:")
    u = [[0 for _ in range(n)] for _ in range(n)]
    l = [[0 for _ in range(n)] for _ in range(n)]
    x = [0] * n
    y = [0] * n

    start = time.perf_counter()

    for i in range(n):
        for j in range(n):
            u[i][j] = a[i][j]

    for k in range(1, n):
        for i in range(k - 1, n):
            for j in range(i, n):
                l[j][i] = u[j][i] / u[i][i]
        for i in range(k, n):
            for j in range(k - 1, n):
                u[i][j] -= l[i][k - 1] * u[k - 1][j]

    for i in range(n):
        for j in range(0, i):
            y[i] -= y[j] * l[i][j]
        y[i] += b[i]
        if y[i] != 0:
            y[i] /= l[i][i]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            x[i] -= x[j] * u[i][j]
        x[i] += y[i]
        if u[i][i] != 0:
            x[i] /= u[i][i]

    print("Time roots counting: {0} milliseconds".format((time.perf_counter() - start) * CONVERT_TO_MILLSEC))

    # print("L = {0}".format(l))
    # print("U = {0}".format(u))
    #
    # print("Input a = {0}".format(a))
    print("Result x = {0}\n".format(x))

    d = [0] * n
    for i in range(n):
        for j in range(n):
            d[i] += a[i][j] * x[j]
    print(d)
    return x
