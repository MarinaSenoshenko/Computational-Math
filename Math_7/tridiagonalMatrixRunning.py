import time

CONVERT_TO_MILLSEC = 1000


def tridiagonalMatrixRunning(matrix, d):
    print("tridiagonalMatrixRunning method:")
    n = len(matrix)
    x = [0] * n
    ksi = [0] * n
    nu = [0] * n

    a = [0] * n
    b = [0] * n
    c = [0] * n

    for i in range(n):
        if i != 0:
            a[i] = matrix[i][i - 1]
        b[i] = matrix[i][i]
        if i != n - 1:
            c[i] = matrix[i][i + 1]

    for i in range(n):
        if abs(b[i]) < abs(a[i]) + abs(c[i]):
            # print("this matrix DOESN'T SATISFIES the convergence condition\n")
            return 0
    # print("this matrix SATISFIES the convergence condition")

    start = time.perf_counter()

    for i in range(n):
        if i == 0:
            ksi[0] -= c[0] / b[0]
            nu[0] = d[0] / b[0]
        else:
            if i != n - 1:
                ksi[i] -= c[i] / (b[i] + a[i] * ksi[i - 1])
            nu[i] -= (a[i] * nu[i - 1] - d[i]) / (b[i] + a[i] * ksi[i - 1])

    x[n - 1] = nu[n - 1]

    for i in range(n - 1, 0, -1):
        x[i - 1] = ksi[i - 1] * x[i] + nu[i - 1]

    print("Time roots counting: {0} milliseconds".format((time.perf_counter() - start) * CONVERT_TO_MILLSEC))

    # print("Input a = {0}".format(a))
    print("Result x = {0}\n".format(x))

    d = [0] * n
    for i in range(n):
        for j in range(n):
            d[i] += matrix[i][j] * x[j]
    print(d)

    return x
