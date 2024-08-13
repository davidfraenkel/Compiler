import sys
sys.path.append('../../')
from Array import Array
import random

def BUBBLESORT(A):
    for i in range(1, len(A) - 1 + 1):
        for j in range(len(A), i + 1 - 1, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

