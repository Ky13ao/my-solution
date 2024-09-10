# n = int(input())
# a = list(map(int, input().split()))
n, a = 8, [1, 4, 2, 1, 4, 6, 2, 7]  
b = [1] * n
t = [0] * n
kq = [0] * n

for i in range(1, n):
    for j in range(i):
        if a[i] >= a[j] and b[j] + 1 > b[i]:
            b[i] = b[j] + 1
            t[i] = j

csMax = 0
for i in range(1, n):
    if b[csMax] < b[i]:
        csMax = i

k = b[csMax]
for i in range(k - 1, -1, -1):
    kq[i] = a[csMax]
    csMax = t[csMax]

for i in range(k):
    print(kq[i], end=" ")

