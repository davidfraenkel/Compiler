import sys
sys.path.append('../../')
from Array import Array
import random

def Greedy_Activity_Selector(s, f):
    n = len(s)
    A = {a[1]}
    k = 1
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            A = A.union({a[m]})
            k = m
    return A

