import sys
sys.path.append('../../')
from Array import Array
import random

def MATRIX_CHAIN_ORDER(p):
    n = len(p) - 1
    m = Array([Array([0 for _ in range(1, n + 1)]) for _ in range(1, n + 1)])
    s = Array([Array([0 for _ in range(1, n - 1 + 1)]) for _ in range(2, n + 1)])
    for i in range(1, n + 1):
        m[i][i] = 0
    for l in range(2, n + 1):
        for i in range(1, n - l + 1 + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j - 1 + 1):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

