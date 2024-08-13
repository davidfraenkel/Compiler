import sys
sys.path.append('../../')
from Array import Array
import random

def TREE_SEARCH(x, k):
    if x == None or k == x.key:
        return x
    if k < x.key:
        return TREE_SEARCH(x.left, k)
    else:
        return TREE_SEARCH(x.right, k)
def TREE_INSERT(T, z):
    y = None
    x = T
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T = z
    elif (z.key < y.key):
        y.left = z
    else:
        y.right = z
def TREE_MAXIMUM(x):
    while x.right != None:
        x = x.right
    return x
def TREE_MINUMUM(x):
    while x.left != None:
        x = x.left
    return x

