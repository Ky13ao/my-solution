# Enter your code here. Read input from STDIN. Print output to STDOUT
A,n = set(input().split()),int(input())
print(sum(set(input().split()) - A == set() for _ in range(n))==n)