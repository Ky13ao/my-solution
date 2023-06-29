# Uses python3
import sys
'''Lab2.5 Giới thiệu bài toán
Bạn sắp tổ chức một cuộc thi thú vị cho trẻ em. Quỹ giải thưởng bạn có là n chiếc kẹo. Bạn muốn dùng những chiếc kẹo này để trao cho 𝑘 vị trí dẫn đầu trong cuộc thi với điều kiện là vị trí cao hơn sẽ nhận được nhiều kẹo hơn. Để khiến nhiều đứa trẻ vui vẻ nhất có thể, bạn sẽ phải tìm ra giá trị k lớn nhất.
          Mô tả bài toán
- Nhiệm vụ. Mục tiêu của bài toán này là biểu diễn một số nguyên dương n dưới dạng tổng của nhiều số nguyên dương khác nhau từng đôi một nhất có thể. Hay, tìm số k lớn nhất sao cho n có thể viết thành 𝑎1 + 𝑎2 + · · · + 𝑎𝑘 trong đó 𝑎1, . . . , 𝑎𝑘 là các số nguyên dương và 𝑎𝑖 ̸= 𝑎𝑗 với mọi 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
- Định dạng input. Input chứa duy nhất một số nguyên n.
- Ràng buộc. 1 ≤ 𝑛 ≤ 10^9
- Định dạng output. Ở dòng đầu tiên, xuất ra giá trị k lớn nhất sao cho n có thể biểu diễn dưới dạng tổng của k số nguyên dương khác nhau từng đôi một. Ở dòng thứ hai, xuất ra k số nguyên dương khác nhau từng đôi một có tổng là n (nếu có nhiều trường hợp như vậy, hãy xuất ra bất kỳ giá trị nào).
- Giới hạn thời gian. 5s
- Giới hạn bộ nhớ. 512MB.
'''
def optimal_summands(n):
  summands = []
  #write your code here
  k=1
  # Nếu số kẹo còn lại > k thì gán k
  while n-k>k:
    summands.append(k)
    n-=k
    k+=1
  # Nếu vẫn còn thì chia hết phần còn lại, số này chắc chắn bé hơn a[k]
  if n>0:
    summands.append(n)
  return summands

if __name__ == '__main__':
  # input = sys.stdin.read()
  n = int(input())
  summands = optimal_summands(n)
  print(len(summands))
  for x in summands:
    print(x, end=' ')