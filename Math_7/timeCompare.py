from GaussZeydel import GaussZeydel
from LUdecompozition import LUDecompozition
from tridiagonalMatrixRunning import tridiagonalMatrixRunning
from HoleskyDecompozition import holeskyDecompozition

a = [[20, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 20, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 10, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 10, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 4, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 3, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 4, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 2, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 2, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 10]]

b = [3, 4, 3, 3, 3, 3, 3, 3, 4, 2]

LUDecompozition(a, b, len(a))
GaussZeydel(a, b, len(a), 0.0001)
tridiagonalMatrixRunning(a, b)
holeskyDecompozition(a, b, len(a))
