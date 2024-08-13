from Array import Arraysys.path.append('../../')
from Array import Array

def MERGE_SECOUND(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L[range(1, n_1 + 1)], L[range(1, n_1 + 1)] = Array([])
    for i in range(1, n_1 + 1):
        L[i] = A[p + i - 1]
    for j in range(1, n_2 + 1):
        R[j] = A[q + j]
    L[n_1 + 1] = 1
    R[n_2 + 1] = 1
    i = 1
    j = 1
    for k in range(p, R + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

