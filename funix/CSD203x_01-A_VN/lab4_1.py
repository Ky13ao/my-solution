# Uses python3
import sys
''' lab4.1
    Giới thiệu bài toán
Bạn được cung cấp một máy tính nguyên thủy có thể thực hiện ba phép tính sau với số x hiện tại: nhân x với 2, nhân x với 3 hoặc cộng 1 vào x. Cho một số nguyên dương n, mục tiêu của bạn là tìm số phép toán tối thiểu cần thiết để có được số n, bắt đầu từ số 1.
    Mô tả bài toán
- Nhiệm vụ. Cho một số nguyên dương n, tính số phép toán tối thiểu để có được số n bắt đầu từ số 1.
- Định dạng input. Input chứa duy nhất một số nguyên thỏa mãn 1 ≤ n ≤ 10^6.
- Định dạng output. Ở dòng đầu tiên, xuất ra số phép tính tối thiểu cần thiết k để thu được giá trị n từ 1. Ở dòng thứ hai, xuất ra một dãy các số trung gian. Hay, dòng thứ hai chứa các số nguyên dương a0, a1, . . . , ak−1 sao cho 0 = 1, ak−1= n 
và với mọi  0 ≤ i < k − 1, a[i+1] bằng a[i]+1, 2a[i] hoặc 3a[i]. Nếu tồn tại nhiều dãy như vậy, xuất ra một dãy bất kỳ.
- Giới hạn thời gian. 5s
- Giới hạn bộ nhớ. 512Mb.
    Cách tiến hành
Mục tiêu của bạn là thiết kế và triển khai giải thuật quy hoạch động cho bài toán này. Một bài toán con trong trường hợp này là: C(n) là số phép tính tối thiểu cần có để đạt được giá trị n từ 1 (sử dụng ba phép toán nguyên thủy). Làm thế nào để biểu diễn C(n) từ C(n/3), C(n/2), C(n−1)?
'''
def optimal_sequence(n):
  # write your code here
  cache = [0 for _ in range(n+1)]
  cache[1] = 1
  for i in range(1, n+1):
    if cache[i]!=0:
      if i+1<n+1 and (cache[i+1]==0 or cache[i+1]>cache[i]+1):
        cache[i+1]=cache[i]+1
      if i*2<n+1 and (cache[i*2]==0 or cache[i*2]>cache[i]+1):
        cache[i*2]=cache[i]+1
      if i*3<n+1 and (cache[i*3]==0 or cache[i*3]>cache[i]+1):
        cache[i*3]=cache[i]+1
  sequence = []
  while n>=1:
    sequence.append(n)
    if cache[n-1]==cache[n]-1:
      n-=1
    elif n%2==0 and cache[n//2]==cache[n]-1:
      n//=2
    elif n%3==0 and cache[n//3]==cache[n]-1:
      n//=3

  return sequence[::-1]

# input = sys.stdin.read()
n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
  print(x, end=' ')