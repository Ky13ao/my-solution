#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
  hrGlass = 0
  sixteenHGs = []
  for r in range(1,5):
    for c in range(1,5):
      s = 0
      for i in range(-1,2):
        if(i!=0):
          for j in range(-1,2):
            s += arr[i+r][j+c]
        else:
          s += arr[r][c]
      sixteenHGs.append(s)
  return max(sixteenHGs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
