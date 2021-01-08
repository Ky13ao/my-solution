def maximumInSlidingWindow(a,k):
  if k==1: return a
  n = len(a)
  if k==n: return [max(a)]
  max_slide = []
  for i in range(n-k+1):
    max_slide.append(a[i:k+i])
  return max_slide
  


import time
a,k = [90,66,49,84,14],2
start = time.time()
print(maximumInSlidingWindow(a,k))
end = time.time()
print('%.10f' % (end - start))