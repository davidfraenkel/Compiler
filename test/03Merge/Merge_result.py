import sys
sys.path.append('../../')
from Array import Array
import random

def MERGE(A, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q
    L = Array([0 for _ in range(1, n_1 + 1 + 1)])
    R = Array([0 for _ in range(1, n_2 + 1 + 1)])
    for i in range(1, n_1 + 1):
        L[i] = A[p + i - 1]
    for j in range(1, n_2 + 1):
        R[j] = A[q + j]
    L[n_1 + 1] = float('inf')
    R[n_2 + 1] = float('inf')
    i = 1
    j = 1
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

