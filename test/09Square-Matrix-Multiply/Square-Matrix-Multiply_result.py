import sys
sys.path.append('../../')
from Array import Array
import random

def SQUARE_MATRIX_MULTIPLY(A, B):
    n = len(A)
    C = Array([Array([0 for _ in range(n)]) for _ in range(n)])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            C[i][j] = 0
            for k in range(1, n + 1):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

