#Cho mảng arr gồm các số nguyên dương và 2 số nguyên dương l và r. Hãy đếm xem có bao nhiêu số i sao cho l<=i<=r và i chia hết cho tất cả các số nằm trong arr.
#Ví dụ:
#Với arr = [2,3] và l = 5, r = 15 thì countNumber(arr,l,r)=2.
#Giải thích: các số cần tìm là: 6, 12.
#Với arr = [2,4,6] và l = 1, r = 36 thì countNumber(arr,l,r)=3.
#Giải thích: các số cần tìm là : 12,24,36.
#Đầu vào/Đầu ra:
#[Thời gian] 0.1s với C++, 0.6s với Java và C#, 0.8s với Python, Go và JavaScript
#[Đầu vào]array of integers
#1<=|a|<=10000.
#0<=a[i]<=40.
#[Đầu vào]long long
#0<=l<=r<=10^18
#[Đầu ra]long long

def _gcd(a,b):
  if b==0: return a
  return _gcd(b,a%b)
def _lcm(a,b):
  return a*b//_gcd(a,b) 
def countNumber(arr,l,r):
  if 0 in arr: return 0
  pot = arr[0]
  for i in arr[1:]:
    if i>1:
      pot=_lcm(i,pot)
    if l==r:
      return 1 if r%pot==0 else 0
  x = r//pot
  y = l//pot
  y += 1 if (y*pot!=l) else 0
  return x - y + 1

import time
arr,l,r = [4,1,2,3],1,100
start = time.time()
print(countNumber(arr,l,r))
end = time.time()
print('%.10f' % (end - start))