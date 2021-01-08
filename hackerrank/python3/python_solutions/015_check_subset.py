# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
  a, A = int(input()),set(input().split())
  b, B = int(input()),set(input().split())
  A-=B
  print(A==set())