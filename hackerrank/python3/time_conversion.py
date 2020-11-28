#!/bin/python3
import os
import sys
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hourNo = int(s[:2])
    if hourNo == 12:
        hourNo-=12
    if s[-2:] == 'PM':
        hourNo+=12
    return "{:02d}".format(hourNo) + s[:-2][2:]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()