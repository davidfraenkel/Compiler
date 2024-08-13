import sys
sys.path.append('../../')
from Array import Array
import random

def MEMOIZED_MATRIX_CHAIN(p):
    n = len(p) - 1
    m = Array([Array([0 for _ in range(1, n + 1)]) for _ in range(1, n + 1)])
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            m[i][j] = float('inf')
    return LOOKUP_CHAIN(m, p, 1, n)
def LOOKUP_CHAIN(m, p, i, j):
    if m[i][j] < float('inf'):
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j - 1 + 1):
            q = LOOKUP_CHAIN(m, p, i, k) + LOOKUP_CHAIN(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]

