import sys
sys.path.append('../../')
from Array import Array
import random

def extended_bottom_up_cut_rod(p, n):
    r = Array([0 for _ in range(0, n + 1)])
    s = Array([0 for _ in range(0, n + 1)])
    r[0] = 0
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r ,  s

print("-------------Extended bottom up cut rod-------------")
def print_cut_rod_solution(p, n):
	"""Print how far apart to cut."""
	r, s = extended_bottom_up_cut_rod(p, n)
	while n > 0:
		print(s[n], end=" ")  # cut location for length n
		n -= s[n]  # length of the remainder of the rod
	print()

prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print_cut_rod_solution(prices, 4)   # should be 2, 2
print_cut_rod_solution(prices, 10)  # should be 10
print()
r, s = extended_bottom_up_cut_rod(prices, 10)
print(r)
print(s)
print()