# Enter your code here. Read input from STDIN. Print output to STDOUT
def aWeightedMean(n, x, w):
  res = 0
  for i in range(n):
    res += x[i] * w[i]
  return res/sum(w)

objs_count = int(input())
obj1s = list(map(int, input().rstrip().split()))
obj2s = list(map(int, input().rstrip().split()))

print('{:.1f}'.format(aWeightedMean(objs_count,obj1s,obj2s)))