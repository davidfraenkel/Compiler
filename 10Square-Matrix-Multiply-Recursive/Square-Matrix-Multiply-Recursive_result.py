import sys
sys.path.append('../../')
from Array import Array
import random

def SQUARE_MATRIX_MULTIPLY_RECURSIVE(A, B):
    n = len(A)
    C = Array([Array([0 for _ in range(n)]) for _ in range(n)])
    if n == 1:
        C[1][1] = A[1][1] * B[1][1]
    else:
        C[1][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1], B[1][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][2], B[2][1])
        C[1][2] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][1], B[1][2]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[1][2], B[2][2])
        C[2][1] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[2][1], B[1][1]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[2][2], B[2][1])
        C[2][2] = SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[2][1], B[1][2]) + SQUARE_MATRIX_MULTIPLY_RECURSIVE(A[2][2], B[2][2])
    return C

