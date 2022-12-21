from common.params import *
from visualize.view import Visualizer
# from first_order.godunov_scheme import Approximator
# from second_order.crank_nikolson import Approximator
from first_order.godunov_scheme_hard import Approximator
# from second_order.crank_nikolson_hard import Approximator


class Controller(object):
    def __init__(self, kff):
        α = kff
        for i in range(4):
            print("r = {0}, tao = {1}, h = {2}".format(r, (r / kff) * hInitial / pow(2, i), hInitial / pow(2, i)))

        Visualizer(Approximator(hInitial, int((A + abs(x_0)) / hInitial), (r / kff) * hInitial),
                   Approximator(hInitial / 2, int((A + abs(x_0)) / (hInitial / 2)), (r / kff) * (hInitial / 2)),
                   Approximator(hInitial / 4, int((A + abs(x_0)) / (hInitial / 4)), (r / kff) * (hInitial / 4)),
                   Approximator(hInitial / 8, int((A + abs(x_0)) / (hInitial / 8)),
                                (r / kff) * (hInitial / 8))).showGraphic()



