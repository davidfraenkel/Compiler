import sys
sys.path.append('../../')
from Array import Array
import random

def Randomize_In_Place(A):
    n = len(A)
    for i in range(1, n + 1):
        A[i], A[random.randint(i, n)] = A[random.randint(i, n)], A[i]

