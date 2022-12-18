from common.params import *
from visualize.view import Visualizer
from first_order.godunov_scheme import Approximator
from second_order.crank_nikolson import Approximator
from first_order.godunov_scheme_hard import Approximator
from second_order.crank_nikolson_hard import Approximator


if r >= 1:
    raise ValueError('Incorrect r')

Visualizer(Approximator(hInitial, int(A / hInitial), (r / α) * hInitial),
           Approximator(hInitial / 2, int(A / (hInitial / 2)), (r / α) * (hInitial / 2)),
           Approximator(hInitial / 4, int(A / (hInitial / 4)), (r / α) * (hInitial / 4)),
           Approximator(hInitial / 8, int(A / (hInitial / 8)), (r / α) * (hInitial / 8))).showGraphic()

