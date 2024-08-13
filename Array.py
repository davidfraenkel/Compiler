#For safe keeping
#import sys
#sys.path.append('../')
#from Array import Array

#If a parameter is an array or matrix, implement arra as A = Array(arra)


class Array(object):

    def __init__(self, items: list) -> None:
        self.items = items

    def __repr__(self) -> str:
        return '{}({})'.format(self.__class__.__name__, self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __contains__(self, item: any) -> bool:
        return item in self.items

    def __getitem__(self, key: int) -> any:
        if isinstance(key, tuple):
            i, j = key
            return self.items[i - 1][j - 1]
        return self.items[key - 1]

    def __setitem__(self, key: int, value: any) -> None:
        if isinstance(key, tuple):
            i, j = key
            self.items[i - 1][j - 1] = value
        else:
            self.items[key - 1] = value

    def __delitem__(self, key: int) -> None:
        if isinstance(key, tuple):
            i, j = key
            del self.items[i - 1][j - 1]
        else:
            del self.items[key - 1]
    
    def __eq__(self, other):
        Array(other)
        for i in range(1, len(self.items)):
            if self.items[i] != other.items[i]:
                return False
        return True
