#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
  freq = dict()
  for c in a:
    if c in freq:
      freq[c] += 1
    else:
      freq[c] = 1
  for c in b:
    if c in freq:
      freq[c] -=1
    else:
      freq[c] =-1
  sum_diff=0
  for c in freq.keys():
    sum_diff += abs(freq[c])
  return sum_diff
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
