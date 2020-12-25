# Enter your code here. Read input from STDIN. Print output to STDOUT
lenList = int(input())
phoneBook = {k: v for k,v in [input().split() for _ in range(lenList)]}
while True:
  try:
    name = input()
    if name in phoneBook:
      print('%s=%s' % (name,phoneBook[name]))
    else:
      print('Not found')
  except:
    break
