#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    count = 0
    if a != sorted(a):
        for i in range(n):
            for j in range(i):
                if a[i]<a[j]:
                    a[i],a[j] = a[j],a[i]
                    count +=1
    print('Array is sorted in {0} swaps.'.format(count))
    print('First Element: {0}'.format(a[0]))
    print('Last Element: {0}'.format(a[n-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
