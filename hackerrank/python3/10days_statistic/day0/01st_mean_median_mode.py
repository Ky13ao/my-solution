# Enter your code here. Read input from STDIN. Print output to STDOUT
objs_count = int(input())
objs = list(map(int, input().rstrip().split()))

meanValue = sum(objs)/objs_count

objs.sort(reverse=False)
medianIndex = int(objs_count / 2)
medianValue = (objs[medianIndex] + objs[medianIndex - 1]) / 2
print(meanValue)
print(medianValue)

def modeValue(arr):
  countsArr = []
  for i in range(len(arr)):
    countsArr.append(sum(a==arr[i] for a in arr))
  resultsArr = []  
  for i in range(len(arr)):
    if countsArr[i] == max(countsArr):
      resultsArr.append(arr[i])
  return min(resultsArr)

print(modeValue(objs))