from common.params import M


def setOrder(approximator):
    for j in range(1, M + 1):
        approximator.u[j][0] = approximator.u[0][0]
        approximator.u[j][1] = approximator.u[0][1]
        approximator.u[j][approximator.N] = approximator.u[0][approximator.N]
        approximator.u[j][approximator.N - 1] = approximator.u[0][approximator.N - 1]
        approximator.u[j][approximator.N - 2] = approximator.u[0][approximator.N - 2]