# Uses python3
import sys
'''2-2.py Mô tả bài toán
Nhiệm vụ. Mục tiêu của bài toán này là triển khai một thuật toán cho bài toán cái túi dạng phân số.
Định dạng input. Dòng đầu tiên của input chứa 𝑛 số vật phẩm và sức chứa 𝑊 của cái túi.
Các dòng 𝑛 tiếp theo biểu thị giá trị và trọng lượng của các vật phẩm. Dòng thứ 𝑖 chứa các số nguyên 𝑣𝑖 và 𝑤𝑖 —tương ứng với giá trị và trọng lượng của vật phẩm thứ 𝑖.
Ràng buộc. 1 ≤  𝑛 ≤ 10³
,          0 ≤ 𝑊 ≤ 2 · 10⁶
;          0 ≤ 𝑣𝑖 ≤ 2 · 10⁶
,          0 < 𝑤𝑖 ≤ 2 · 10⁶
với mọi 1 ≤ 𝑖 ≤ 𝑛. Tất cả các số là số nguyên.
Định dạng output. Xuất ra giá trị phân số tối đa của các vật phẩm có thể cho vừa vào cái túi. Giá trị tuyệt đối của hiệu giữa kết quả từ chương trình của bạn và giá trị tối ưu lớn nhất là 10^−3. Để đảm bảo điều này, xuất ra kết quả với ít nhất 4 chữ số sau dấu thập phân (nếu không, kết quả của bạn, dù được tính toán chính xác, vẫn có thể bị sai do làm tròn).
Giới hạn thời gian. 5s
Giới hạn bộ nhớ. 512MB.
'''

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    pack = sorted(zip(values, weights), reverse=True)
    for v, w in pack:
      while capacity>=w:
        value+=v
        capacity-=w
    if capacity>0:
      return pack[0][0]/pack[0][1]*capacity
    return value


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # data = list(map(int, input().split()))
    data = [3, 50, 60, 20, 100, 50, 120, 30]
    # data = [1, 10, 500, 30]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))