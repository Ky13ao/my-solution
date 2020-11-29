# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def standardDeviation(n, ls):
  dev = sum(ls)/n
  res = sum(pow(i - dev,2) for i in ls)
  return math.sqrt(res/n)

objs_count = int(input())
objs = list(map(int, input().rstrip().split()))

print('{:.1f}'.format(standardDeviation(objs_count,objs)))