#Uses python3

import sys
'''2-3.py ·   Giới thiệu bài toán
Bạn có 𝑛 quảng cáo cần được bố trí ở 𝑛 vị trí khác nhau lên internet. Với mỗi cú nhấp chuột vào quảng cáo, bạn sẽ nhận được một số tiền tương ứng với quảng cáo đó. Để tối đa hóa doanh thu, bạn sẽ cần phải thiết lập 𝑛 vị trí với 𝑛 quảng cáo.
          ·    Mô tả bài toán
Nhiệm vụ. Cho hai dãy 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 là lợi nhuận trên một cú nhấp chuột vào quảng cáo thứ 𝑖) và 𝑏1, 𝑏2, ..., 𝑏𝑛 (bi  là số lượng cú nhấp chuột trung bình một ngày ở vị trí thứ 𝑖), chúng ta cần chia chúng thành 𝑛 cặp (𝑎𝑖, 𝑏j) sao cho tổng của doanh thu là tối đa.
Định dạng input. Dòng đầu tiên chứa một số nguyên 𝑛, dòng thứ hai chứa 1 dãy các số nguyên 𝑎1, 𝑎2, …, 𝑎𝑛, dòng thứ ba chứa một dãy các số nguyên 𝑏1, 𝑏2, . . . , 𝑏𝑛.
Ràng buộc. 1 ≤ 𝑛 ≤ 10^3 ; −10^5 ≤ 𝑎𝑖 , 𝑏𝑖 ≤ 10^5 với mọi 1 ≤ 𝑖 ≤ 𝑛.
Định dạng output. Xuất ra giá trị tối đa của tổng aici khi 𝑖 chạy từ 1 đến 𝑛 và c1, c2, … c𝑛 là một hoán vị của 𝑏1, 𝑏2, . . . , 𝑏𝑛.
Giới hạn thời gian: 5s
Giới hạn bộ nhớ: 512MB
'''
def max_dot_product(a, b):
    #write your code here
    res = 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    # input = sys.stdin.read()
    data = list(map(int, input().split()))
    # data = [1, 23, 39]
    # data = [3, 1, 3, -5, -2, 4, 1]
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))