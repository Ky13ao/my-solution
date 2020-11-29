# Enter your code here. Read input from STDIN. Print output to STDOUT
def medianValue(ls):
  n = len(ls)
  if n<2:
    return sum(ls)
  else:
    i = int(n / 2)
    if n % 2 == 0:
      return (ls[i] + ls[i - 1]) / 2
    else:
      return ls[i]

def setS(x,f):
  resSet = []
  for i in range(len(x)):
    for j in range(f[i]):
      resSet.append(x[i])
  return resSet

def interQuartiles(ls):
  n = len(ls)
  ls.sort()
  half = int(n/2)
  lhalf = []
  uhalf = []
  for i in range(n):
    if i<half:
      lhalf.append(ls[i])
    elif i>n-half-1:
      uhalf.append(ls[i])
  return abs(medianValue(lhalf) - medianValue(uhalf))

objs_count = int(input())
objs = list(map(int, input().rstrip().split()))
objs2 = list(map(int, input().rstrip().split()))

objs = setS(objs,objs2)
print('{:.1f}'.format(interQuartiles(objs)))