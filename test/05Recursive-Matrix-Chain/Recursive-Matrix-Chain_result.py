import sys
sys.path.append('../../')
from Array import Array
import random

def RECURSIVE_MATRIX_CHAIN(P, i, j, m):
    if i == j:
        return 0
    m[i][j] = float('inf')
    for k in range(i, j - 1 + 1):
        q = RECURSIVE_MATRIX_CHAIN(P, i, k, m) + RECURSIVE_MATRIX_CHAIN(P, k + 1, j, m) + P[i - 1] * P[k] * P[j]
        if q < m[i][j]:
            m[i][j] = q
    return m[i][j]

