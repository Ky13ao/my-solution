from lib import *

def exercise_2_1(l):
  l = quickSort(l, reverse=True)
  maxK = 0
  for i, item in enumerate(l):
    k = item+i+1
    if maxK<k:
      maxK = k
  print(maxK)

def exercise_2_2(l):
  l = quickSort(l, reverse=True)
  stiffNess = l[0]
  k = 1
  for item in l[1:]:
    stiffNess-=1
    k+=1
    if stiffNess>item:
      stiffNess=item
    if stiffNess==0:
      print(k)
      return
  print(len(l))

def exercise_3_1(l, x):
  def count(arr, x):
    if len(arr)==1:
      if arr[0]==x:
        return 1
      else:
        return 0
    else:
      midIdx = len(arr)//2
      print(arr, midIdx, ';  ', end=' ')
      return count(arr[:midIdx], x) + count(arr[midIdx:], x)
  print(count(l, x))

def exercise_3_2(l, x):
  def linearSearch(arr, x):
    for i, a in enumerate(arr):
      if a==x:
        return i
    return -1
  print(linearSearch(l, x))

def exercise_4_1_74(l):
  cache = [1]
  iMax = 0
  for i in range(1, len(l)):
    if l[i]>l[i-1]:
      cache.append(cache[i-1]+1)
    else:
      cache.append(1)
    if cache[iMax]<cache[i]:
      iMax=i
  for _ in l[iMax-cache[iMax]+1:iMax+1]:
    print(_, end=' ')

def exercise_4_1_75(l, x):
  cache = [1 if _ in l else 0 for _ in range(x+1)]
  for i in range(1, x+1):
    for il in l:
      if i>il:
        if (cache[i]>cache[i-il]+1 and cache[i-il] != 0) \
          or (cache[i]==0 and cache[i-il]!=0):
          cache[i]=cache[i-il]+1
  print(cache[x])

def exercise_4_1_76(l):
  cacheS = [[l[0],-1]]
  for i in range(1, len(l)):
    cacheS.append([l[i], -1])
    for j in range(i):
      if l[j]==l[i] and cacheS[j][0]+l[i]>cacheS[i][1]:
        cacheS[i][1]=cacheS[j][0]+l[i]
    for j in range(i):
      if cacheS[j][1]+l[i]>cacheS[i][0]:
        cacheS[i][0]=cacheS[j][1]+l[i]
  print(max([max(s) for s in cacheS]))

def exercise_5_1_47(l):
  l = quickSort(l)
  if l[0]>0:
    print(0)
    return
  m = 0
  for i in range(len(l)):
    if m+1==l[i]:
      m=l[i]
  print(m+1)

def exercise_5_1_48(l):
  l = quickSort(l)
  idx = 0
  m = idx
  while idx<len(l):
    if l[idx]!=l[m]:
      print(l[m], idx-m, end='; ')  
      m = idx
    idx+=1
  print(l[m], idx-m, end='; ')
      
def exercise_5_1_49(l, k):
  l = quickSort(l)
  count = 0
  for i in range(1, len(l)):
    if l[i]-l[i-1]>k:
      count+=1
  print(count+1)

def exercise_5_1_50(l):
  def isPow(n):
    sqrt = n**(1/2)
    if sqrt==int(sqrt):
      return True
    return False
  l = [_ for _ in l if isPow(_)]
  if len(l)==0:
    print('NULL')
    return
  after = quickSort(l)
  m = after[0]-1
  for i in after:
    if i!=m:
      print(i, end=' ')
      m = i

def exercise_5_1_51(l):
  b = [_ for _ in l if _!=0]
  if len(b)==0:
    print(*l)
    return
  b = quickSort(b)
  for i in range(len(l)-1, -1, -1):
    if l[i] < 0:
      l[i] = b[0]
      del b[0]
  for i in range(len(l)):
    if l[i] > 0:
      l[i] = b[0]
      del b[0]
  print(*l)

if __name__=='__main__':
  # l = list(map(int, input().strip().split(',')))
  # l = main([int(input()) for _ in range(int(input())) ])
  # exercise_3_2([1,2,3,5,6,1,3,5,1,3,5,78,1,2,4,5,1], 5)
  # exercise_4_1_74([1, 2, 1, 4, 5, 6, 2])
  # exercise_4_1_75([1, 2, 8, 10], 25)
  # exercise_4_1_75([1, 5, 7], 32)
  # exercise_4_1_76([10, 6, 7, 6, 1])
  # exercise_4_1_76([2,5,2,6,1,6,2])
  # exercise_5_1_47([0, 0, 1, 4, 2, 4, 3])
  # exercise_5_1_48([-3, -3, 2, 4, 2, 2, 6])
  # exercise_5_1_48([3, 3, 3])
  # exercise_5_1_49([1, 3, 2, 5, 10, 8], 2)
  # exercise_5_1_49([7, 5, 8, 9], 3)
  # exercise_5_1_50([9, 1, 2, 3, 1])
  # exercise_5_1_50([2, 3, 5])
  exercise_5_1_51([3, -1, 2, 0, -4, 6])
  exercise_5_1_51([0, 0 , 0])