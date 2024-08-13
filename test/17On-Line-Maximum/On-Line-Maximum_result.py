import sys
sys.path.append('../../')
from Array import Array
import random

def score(i):
    n = random.randint(0, 100)
    return n
def ON_LINE_MAXIMUM(k, n):
    bestscore = float('-inf')
    for i in range(1, k + 1):
        if score(i) > bestscore:
            bestscore = score(i)
    for i in range(k + 1, n + 1):
        if score(i) > bestscore:
            return i
    return n

