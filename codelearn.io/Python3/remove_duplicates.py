def removeDuplicates(arr):
  freq = {}
  for n in arr:
    if n in freq:
      if freq[n] <2:
        freq[n] += 1
    else:
      freq[n] = 1
  return sum(freq.values())

import time
arr = 2,5,6
start = time.time()
print(removeDuplicates(arr))
end = time.time()
print('%.10f' % (end - start))