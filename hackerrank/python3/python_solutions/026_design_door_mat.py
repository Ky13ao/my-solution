# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
pattern = [('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
print(*(pattern+['WELCOME'.center(m,'-')]+pattern[::-1]),sep='\n')