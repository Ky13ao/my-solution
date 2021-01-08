def fiboSum(n):
  if n == 0: return [-1]
  fibs = [0,1]
  fib_sum = 0
  while fib_sum<n:
    fib_sum+=fibs[-1] + fibs[-2]
    fibs.append(fibs[-1] + fibs[-2])
  m = fib_sum-n
  while m!=0:
    _=1
    while fibs[_+1]<=m: _+=1
    m-=fibs[_]
    fibs[_] = 0
  return [i for i in fibs[2:] if i>0]
  
#Phân tích số nguyên dương thành tổng các số hạng của dãy Fibonaci sao cho có nhiều số hạng nhất (các số hạng không được trùng nhau).
import time
start = time.time()
print(fiboSum(10))
end = time.time()
print('time: %.10f' % (end - start))