#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    sOut = str(arr[len(arr)-1])
    for i in range(len(arr)-1,0,-1):
      sOut += ' ' + str(arr[i-1])
    print(sOut)
      
