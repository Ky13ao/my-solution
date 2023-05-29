# Uses python3
import sys
'''lab4.2
    Giới thiệu bài toán
Bài toán này là về việc triển khai một thuật toán cho bài toán cái túi không lặp lại.
    Mô tả bài toán
Nhiệm vụ. Trong bài toán này, bạn có một chồng các thỏi vàng và mục tiêu của bạn là cho càng nhiều vàng vào túi càng tốt. Mỗi thỏi chỉ có một bản sao và bạn chỉ có thể chọn lấy hoặc không (do đó bạn không thể lấy một phần của một thỏi vàng).
Định dạng input. Dòng đầu tiên bao gồm sức chứa W của cái túi và số lượng n thỏi vàng. Dòng tiếp theo chứa n số nguyên w0, w1, . . . , wn−1 biểu thị trọng lượng của các thỏi vàng.
Ràng buộc. 1 ≤ W ≤ 10^4; 1 ≤ n ≤ 300; 0 ≤ w0, . . . , wn−1 ≤ 10^5.
Định dạng output. Xuất ra trọng lượng tối đa của các thỏi vàng có thể cho vừa vào túi với sức chứa W.
Giới hạn thời gian. 5s
Giới hạn bộ nhớ. 512Mb.
'''
def optimal_weight(W, w):
    # write your code here
    # Khởi tạo mảng cache với Trọng số 0 nghĩa là không lấy gì
    cache=[[True]+[False]*W]
    for i in range(len(w)):
      # Clone mảng boolean gốc
      cache.append(cache[-1][:])
      # Kiểm tra sức chứa từ trọng lượng thỏi vàng đến tổng trọng lượng của túi
      for j in range(w[i], W+1):
        # Vị trí hiện tại có thể lấy nếu như kiểm tra trước đó có thể lấy hoặc sức chứa còn lại cho phép lấy
        cache[-1][j]=cache[-2][j] or cache[-2][j-w[i]]
      cache=cache[-1:]
    # Lấy vị trí chứa hợp lệ lớn nhất
    for i in range(W, -1, -1):
      if cache[-1][i]:
        return i
    

if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input().split()))
    W, w = 10, [1, 4, 8]
    # W, w = 209, [16, 21, 21, 96, 129, 144, 159, 253, 254, 259, 259, 267, 285, 290, 304, 351, 351, 383, 411, 429, 493, 494, 527, 530, 534, 596, 619, 625, 692, 717, 727, 727, 745, 772, 833, 853, 856, 946]
    print(optimal_weight(W, w))