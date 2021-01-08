if __name__ == '__main__':
  ls = []
  for _ in range(int(input())):
    op, *numbers = input().split()
    if op == 'print':
      print(ls)
    else:
      eval('ls.{}{}'.format(op,tuple(map(int,numbers))))
  