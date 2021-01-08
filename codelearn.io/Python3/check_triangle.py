#Nam đang thực hành đo các góc trong tam giác, thu được số đo 3 góc là a, b, c. Hãy kiểm tra xem liệu số đo 3 góc mà Nam thu được có đúng hay không. Nếu có trả về "Right", ngược lại trả về "Wrong".

#Biết tổng các góc của một tam giác luôn là 180 độ và số đo các góc luôn lớn hơn 0 độ.

#Với a = 90, b = 50, c = 40. Đầu ra triangle_angle(a, b, c) = "Right".
#Đây đúng là số đo 3 góc của một tam giác.
#Với a = 120, b = 60, c = 40. Đầu ra triangle_angle(a, b, c) = "Wrong".
#Đây không phải là số đo 3 góc của một tam giác (120 + 60 +40 = 220 mà số đo 3 góc của 1 tam giác luôn phải bằng 180)
#Đầu vào/Đầu ra:

#[Thời gian chạy] 0.5s với C++, 3s với Java và C#, 4s với Python, Go và JavaScript.
#[Đầu vào] Integer a, b, c
#0 <= a, b, c <= 180
#[Đầu ra] String
#Nếu sai trả về chuỗi "Wrong", ngược lại trả về "Right".

def triangle_angle(a,b,c):
  if a*b*c == 0: return 'Wrong'
  if a+b+c != 180: return 'Wrong'
  return 'Right'

import time
a,b,c = 60,60,60
start = time.time()
print(triangle_angle(a,b,c))
end = time.time()
print('%.10f' % (end - start))