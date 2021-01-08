#Cho 3 số nguyên l, r, d. Hãy tìm số nguyên dương x thỏa mãn:

#x không nằm trong đoạn [l, r].
#x chia hết cho d.
#x bé nhất
#Ví dụ:

#Với l = 2, r = 4, d = 2. Đầu ra divisorNumber(x, y, z) = 6.
#     Giải thích: 6 chia hết cho 2 và không nằm trong đoạn [2, 4].

#Đầu vào/Đầu ra:

#[Thời gian chạy] 0.1s với C++, 0.6s với Java và C#, 0.8s với Python, Go và JavaScript.
#[Đầu vào] Integer l, r, d
#      1 <= l < r < INT_MAX

#      1 <= d < INT_MAX

#[Đầu ra] Long long
#Số nhỏ nhất chia hết cho d

def divisorNumber(l,r,d):
  if d<l or d>r: return d
  if d*2<l or d*2>r: return d*2
  return d*(r//d+1)

import time
l,r,d = 2,5,6
start = time.time()
print(divisorNumber(l,r,d))
end = time.time()
print('%.10f' % (end - start))

#2,4,2 => 6
#1,7,6 => 12
#4,6,5 => 10
#11,20,19 => 38