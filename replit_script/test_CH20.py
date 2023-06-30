#Cho mảng các số nguyên arr, bạn hãy viết hàm trả về ước số lớn nhất mà khác chính nó của từng phần tử trong arr.

#Ví dụ
#Với arr = [3, 20, 9] thì output là largestDivisors(arr) = [1, 10, 3].
#Giải thích: ước số lớn nhất mà khác chính nó của 3, 20, 9 lần lượt là [1, 10, 3].
#Với arr = [7, 91, 56] thì output là largestDivisors(arr) = [1, 13, 9].
#Đầu vào/Đầu ra
#[Giới hạn thời gian chạy]: 1s với C++, 4s với Java và C#, 8s với Python, GO và Js
#[Đầu vào] Array of integers arr
#1 <= arr.size <= 1000
#2 <= arr[i] <= 1012
#[Đầu ra] Integer

def largestDivisor(arr):
  output = []
  for n in arr:
    x = n**0.5
    if x==int(x):
      output.append(int(x))
      continue
    ok = False
    for f in range(2,int(x)+1):
      if n%f==0:
        output.append(n//f)
        ok = True
        break
    if not ok:
      output.append(1)
  return output

import time, random
arr = [random.randint(2,10**12) for _ in range(12)]
start = time.time()
print('INPUT',arr)
print('OUTPUT',largestDivisor(arr))
end = time.time()
print('time: %.10f' % (end - start))
