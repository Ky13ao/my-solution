#!/bin/python3

import math
import os
import random
import re
import sys

def sumOfHG(arr, x, y):
  s = sum(arr[x][y:y+3]) + sum(arr[x+2][y:y+3]) + arr[x+1][y+1]
  return s

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    sums = []
    for i in range(4):
      for j in range(4):
        sums.append(sumOfHG(arr,i,j))
        
    print(max(sums))
