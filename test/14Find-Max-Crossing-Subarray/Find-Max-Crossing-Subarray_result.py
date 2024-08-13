import sys
sys.path.append('../../')
from Array import Array
import random

def FIND_MAX_CROSSING_SUBARRAY(A, _low, mid, _high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, _low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(mid + 1, _high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

