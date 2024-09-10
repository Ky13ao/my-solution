# Uses python3
import sys
import random
'''  Giới thiệu bài toán
Mục tiêu trong bài toán này là thiết kế lại một triển khai đã cho của thuật toán Quick Sort (sắp xếp nhanh) ngẫu nhiên để nó thao tác nhanh ngay cả trên các chuỗi chứa nhiều phần tử bằng nhau.
   Mô tả bài toán
- Nhiệm vụ. Để buộc triển khai đã cho của thuật toán Quick Sort xử lý hiệu quả các chuỗi có ít phần tử duy nhất, mục tiêu của bạn là thay thế sắp xếp 2-phân đoạn bằng sắp xếp 3-phân đoạn. Tức là thủ tục sắp xếp mới của bạn sẽ sắp xếp mảng thành ba phần: phần < x, phần = x và phần > x.
- Định dạng input. Dòng đầu tiên của input chứa số nguyên n. Dòng tiếp theo chứa một dãy n số nguyên a0, a1, . . . , an−1.
- Ràng buộc. 1 ≤ n ≤ 10^5 ; 1 ≤ ai ≤ 10^9 với mọi 0 ≤ i < n.
- Định dạng output. Xuất ra chuỗi này sắp xếp theo thứ tự không giảm dần.
- Giới hạn thời gian. 10s
- Giới hạn bộ nhớ. 512Mb.
'''
def partition3(a, l, r):
  #write your code here
  # đầu tiên đặt phần tử là phần tử đầu tiên
  x = a[l]
  # duyệt mảng a từ vị trí `l` --> `r`
  i = l
  while i<=r:
    if a[i] < x:
      # nếu phần tử hiện tại < phần tử chốt thì hoán vị 2 phần tử a[i] a[l]
      # thu hẹp vùng duyệt bằng cách tăng biến `l`
      swap(a, l, i)
      l += 1
      i += 1
    elif a[i]==x:
      # nếu phần tử hiện tại = phần tử chốt thì duyệt tiếp
      i +=1
    else:
      # nếu phần tử hiện tại > phần tử chốt thì hoán vị a[i] a[r]
      # không tăng `i` để xử lý tiếp phần tử ở vị trí `i` hiện tại, vì ko chắc i đã được sắp xếp đúng
      swap(a, i, r)
      r -=1
  return l, r

def swap(a, i, j):
  a[i], a[j] = a[j], a[i]

def partition2(a, l, r):
  x = a[l]
  j = l
  for i in range(l + 1, r + 1):
    if a[i] <= x:
      j += 1
      a[i], a[j] = a[j], a[i]
  a[l], a[j] = a[j], a[l]
  return j


def randomized_quick_sort(a, l, r):
  if l >= r:
    return
  k = random.randint(l, r)
  swap(a, l, k)
  #use partition3
  m1, m2 = partition3(a, l, r)
  # print(a, l, m1, m2, r)
  randomized_quick_sort(a, l, m1-1)
  randomized_quick_sort(a, m2+1, r)

  #use partition2
  # m = partition2(a, l, r)
  # randomized_quick_sort(a, l, m - 1)
  # randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':
  # input = sys.stdin.read()
  # n, *a = list(map(int, input().split()))
  # n, a = 5, [2, 3, 9, 2, 2]
  n, a = 10, [1, -2, 3, 4, -5, 7, -8, -2, 0 ,-9]
  randomized_quick_sort(a, 0, n - 1)
  for x in a:
    print(x, end=' ')
