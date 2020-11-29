#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
  count = len(s)
  for i, char in enumerate(s):
    diff_char_idx = None
    for j in range(i+1, n):
      if char == s[j]:
        if diff_char_idx is None:
          count +=1
        elif j - diff_char_idx == diff_char_idx - i:
          count += 1
          break
      else:
        if diff_char_idx is None:
          diff_char_idx = j
        else:
          break
  return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
