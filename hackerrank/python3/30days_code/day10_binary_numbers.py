#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
  n = int(input())
  cons1 = 0
  max_value = 0
  while n>0:
    if n % 2 == 1:
      cons1 += 1
      if max_value < cons1:
        max_value = cons1
    else:
      cons1 = 0
    n = n // 2

  print(max_value)
