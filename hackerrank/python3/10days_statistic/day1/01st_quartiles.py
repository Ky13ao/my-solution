# Enter your code here. Read input from STDIN. Print output to STDOUT
def medianValue(ls):
  n = len(ls)
  i = int(n / 2)
  if n % 2 == 0:
    return int((ls[i] + ls[i - 1]) / 2)
  else:
    return ls[i]
  
def quartiles(n, ls):
  ls.sort()
  half = int(n/2)
  lhalf = ls[:half]
  uhalf = ls[-half:]
  return (medianValue(lhalf), medianValue(ls), medianValue(uhalf))

objs_count = int(input())
objs = list(map(int, input().rstrip().split()))

print('\n'.join(map(str, quartiles(objs_count,objs))))
