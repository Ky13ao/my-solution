#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):

  def mergeArr(leftArr, rightArr):
    count, leftI, rightI, arr, lenLeftA, lenRightA = 0, 0, 0, [], len(leftArr), len(rightArr)
    while (leftI<lenLeftA)&(rightI<lenRightA):
      if leftArr[leftI]<=rightArr[rightI]:
        arr.append(leftArr[leftI])
        leftI+=1
      else:
        arr.append(rightArr[rightI])
        rightI+=1
        count += lenLeftA-leftI
    arr += leftArr[leftI:]
    arr += rightArr[rightI:]    
    return count, arr
    
  def mergeSort(arr):
    if len(arr)<=1: return 0, arr
    mid = len(arr)//2
    leftSwaps, leftRes = mergeSort(arr[:mid])
    rightSwaps, rightRes = mergeSort(arr[mid:])
    mSwaps, res = mergeArr(leftRes, rightRes)
    return mSwaps + leftSwaps + rightSwaps, res
  
  count, arr = mergeSort(arr)
  return count
      
  
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  t = int(input())

  for t_itr in range(t):
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countInversions(arr)

    fptr.write(str(result) + '\n')

  fptr.close()
