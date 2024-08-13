import sys
sys.path.append('../../')
from Array import Array
import random

def INSERTION_SORT(A):
    for j in range(2, len(A) + 1):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

