def minimumAbsolute(arr):
  a_sorted = sorted(arr)
  n = len(arr)
  min_abs = max(arr)
  for i in range(n-1):
    abs_v = abs(a_sorted[i]-a_sorted[i+1])
    if min_abs>abs_v:
      min_abs=abs_v
  min_abs_ls = []
  for i in range(n-1):
    abs_v = abs(a_sorted[i]-a_sorted[i+1])
    if abs_v==min_abs:
      min_abs_ls.append([a_sorted[i],a_sorted[i+1]])
  return min_abs_ls

import time
arr = [1,10,0,5,7,2,4,9,8,6]
start = time.time()
print(minimumAbsolute(arr))
end = time.time()
print('%.10f' % (end - start))