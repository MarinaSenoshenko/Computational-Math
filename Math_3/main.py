from numpy import linalg as LA

ROWS = 3
COLS = 4


def printMatrix(a):
    for i in range(ROWS):
        print(a[i][0], a[i][1], a[i][2], a[i][3])


def methodGauss(a):
    print("/*************************************/\nMethod Gauss")
    print("step 0: initial matrix:")
    printMatrix(a)

    print("Algorithm:\nstep 1: multiply first row for -a[1][0] / a[0][0] and add to the second row")
    print("step 2: multiply first row for -a[2][0] / a[0][0] and add to the third row")
    print("step 3: 1) multiply second row for -a[2][1] / a[1][1] and add to the third row - if a[1][1] = 0 2) replace second and third rows - else")

    for k in range(ROWS - 1):
        for j in range(k, ROWS - 1):
            print("matrix in step {0}:".format(j + k + 1))
            if a[k][k] != 0:
                alpha = a[j + 1][k] / a[k][k]
                for i in range(COLS):
                    a[j + 1][i] -= alpha * a[k][i]
            else:
                for i in range(COLS):
                    a[k][i], a[k + 1][i] = a[k + 1][i], a[k][i]
            printMatrix(a)

    x = [0] * ROWS
    for i in range(ROWS - 1, -1, -1):
        for j in range(COLS - 2, i, -1):
            x[i] -= x[j] * a[i][j]
        x[i] += a[i][3]
        if a[i][i] != 0:
            x[i] /= a[i][i]

    print("The result of solving the equation:")
    print(x)
    print("cond(A) = {0} (not current)".format(LA.cond([[20, 20, 0], [15, 15, 5], [0, 1, 1]])))
    return x


def f_x(x1, x2, a, ind, first, second):
    return -x1 * a[ind][first] / a[ind][ind] - x2 * a[ind][second] / a[ind][ind] + a[ind][ROWS] / a[ind][ind]


def norm(x1, x2):
    max_cur_row = abs(x1[0] - x2[0])
    norm_x = 0
    for i in range(1, COLS - 1):
        for j in range(1, ROWS):
            max_cur_row += abs(x1[j] - x2[j])
        if max_cur_row > norm_x:
            norm_x = max_cur_row
    return norm_x


def rootExpression(i, i1, i2, el1, el2, el3):
    print("x{0} = {1}*x_{2} + {3}*x_{4} + {5}".format(i + 1, el1, i1 + 1, el2, i2 + 1, el3))


def methodYakobi(a, eps):
    print("/*************************************/\nMethod Yakobi")
    print("step 0: initial matrix:")
    printMatrix(a)

    print("Testing matrix.....")
    sum_non_diagonal = 0

    for i in range(COLS - 1):
        for j in range(ROWS):
            if i != j:
                sum_non_diagonal += abs(a[i][j])
        if abs(a[i][i]) < sum_non_diagonal:
            print("this matrix DON'T SATISFIES the convergence condition")
            return 0
        sum_non_diagonal = 0

    print("this matrix SATISFIES the convergence condition")

    x_0 = [a[0][3] / a[0][0], a[1][3] / a[1][1], a[2][3] / a[2][2]]
    x_new = [0, 0, 0]
    print("step 1: initial vector (divide b by diagonal element from it's row):")
    print("x_{0} = {1} x_{2} = {3} x_{4} = {5}".format(1, x_0[0], 2, x_0[1], 3, x_0[2]))
    print("step 2: express from the system elements x1, x2, x3")

    rootExpression(0, 1, 2, -a[0][1] / a[0][0], -a[0][2] / a[0][0], a[0][3] / a[0][0])
    rootExpression(1, 0, 2, -a[1][0] / a[1][1], -a[1][2] / a[1][1], a[1][3] / a[1][1])
    rootExpression(2, 0, 1, -a[2][0] / a[2][2], -a[2][1] / a[2][2], a[2][3] / a[2][2])

    print("step 3: count while norm_inf(x(n)) - norm_inf(x(n + 1)) > {0}\n........".format(eps))

    while abs(norm(x_0, x_new)) > eps:
        for i in range(ROWS):
            x_0[i] = x_new[i]
        x_new[0] = f_x(x_0[1], x_0[2], a, 0, 1, 2)
        x_new[1] = f_x(x_0[0], x_0[2], a, 1, 0, 2)
        x_new[2] = f_x(x_0[0], x_0[1], a, 2, 0, 1)

    print("The result of solving the equation:")
    print(x_new)
    print("cond(A) = {0} (not current)".format(LA.cond([[2, 1, -1], [1, -5, 4], [3, 2, 6]])))
    return x_new


methodYakobi([[1, 0.5, 1./3., 2], [0.5, 1./3., 0.25, 2], [1./3., 0.25, 0.2, 2]], 0.01)
