if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().rstrip().split()))
  best = max(arr)
  while best in arr:
    arr.remove(best)
  print(max(arr))