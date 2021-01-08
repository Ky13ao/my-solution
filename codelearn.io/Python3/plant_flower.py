def plantFlowers(arr,n):
  if n == 0: return True
  if (len(arr)==1)&(arr[0]==0): return True
  if len(arr)==2&sum(arr)==0: return True
  d = 0
  for i in range(1,len(arr)-1):
    if sum(arr[i-1:i+2])==0:
      d += 1
      if d == n: return True
  if sum(arr[:1])==0: d+=1
  if sum(arr[len(arr)-1:])==0: d+=1
  if d>=n: return True
  return False
  


import time
arr,n = [1, 0, 0, 0, 1],1
start = time.time()
print(plantFlowers(arr,n))
end = time.time()
print('%.10f' % (end - start))