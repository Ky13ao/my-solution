#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
  for t_itr in range(int(input())):
    n, k = map(int,input().rstrip().split())
    print(k-1 if ((k-1) | k) <= n else k-2)