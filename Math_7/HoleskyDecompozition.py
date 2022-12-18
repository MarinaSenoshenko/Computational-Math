import math
import time

CONVERT_TO_MILLSEC = 1000


def holeskyDecompozition(a, b, n):
    c = [[0 for _ in range(n)] for _ in range(n)]
    c_t = [[0 for _ in range(n)] for _ in range(n)]
    x = [0] * n
    y = [0] * n
    print("HoleskyDecompozition method:")
    start = time.perf_counter()
    for j in range(0, n):
        tmp = a[j][j]
        for k in range(0, j):
            tmp -= math.pow(c[j][k], 2)
        c[j][j] = math.sqrt(tmp)
        c_t[j][j] = math.sqrt(tmp)

        for i in range(j + 1, n):
            tmp = a[i][j]
            for k in range(0, j):
                tmp -= c[i][k] * c[j][k]
            c[i][j] = tmp / c[j][j]
            c_t[j][i] = tmp / c[j][j]

    for i in range(n):
        for j in range(0, i):
            y[i] -= y[j] * c[i][j]
        y[i] += b[i]
        y[i] /= c[i][i]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            x[i] -= x[j] * c_t[i][j]
        x[i] += y[i]
        x[i] /= c_t[i][i]

    print("Time roots counting: {0} milliseconds".format((time.perf_counter() - start) * CONVERT_TO_MILLSEC))

    d = [0] * n
    for i in range(n):
        for j in range(n):
            d[i] += a[i][j] * x[j]
    print(d)
    return x
