_ , ls = int(input()) , set(map(int,input().split()))
for _ in range(int(input())):
    op, n = input().split()
    numops = set(map(int, input().split()))
    eval('ls.{}({})'.format(op,numops))
print(sum(ls))