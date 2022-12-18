import time

CONVERT_TO_MILLSEC = 1000


def GaussZeydel(a, b, n, eps):
    print("GaussZeydel method:")
    x_0 = [0] * n
    x_new = [0] * n
    max = 1

    # print("Testing matrix.....")
    sum_non_diagonal = 0

    for i in range(n):
        for j in range(n):
            if i != j:
                sum_non_diagonal += abs(a[i][j])
        if abs(a[i][i]) < sum_non_diagonal:
            # print("this matrix DOESN'T SATISFIES the convergence condition\n")
            return 0
        sum_non_diagonal = 0
    # print("this matrix SATISFIES the convergence condition")

    for i in range(n):
        x_0[i] = b[i] / a[i][i]
        x_new[i] = x_0[i] + 1

    start = time.perf_counter()

    while max >= eps:
        for i in range(n):
            tmp = b[i]
            for j in range(n):
                if j < i:
                    tmp -= a[i][j] * x_new[j]
                if j > i:
                    tmp -= a[i][j] * x_0[j]
            x_new[i] = tmp / a[i][i]
        max = 0
        for i in range(n):
            if abs(x_0[i] - x_new[i]) > max:
                max = abs(x_0[i] - x_new[i])
            x_0[i] = x_new[i]

    print("Time roots counting: {0} milliseconds".format((time.perf_counter() - start) * CONVERT_TO_MILLSEC))

    # print("Input a = {0}".format(a))
    print("Result x = {0} for eps = {1}\n".format(x_new, eps))
    d = [0] * n
    for i in range(n):
        for j in range(n):
            d[i] += a[i][j] * x_new[j]
    print(d)
    return x_new
