# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
'''2-4.py Giới thiệu bài toán
    - Bạn cần lấy chữ ký của tất cả các hộ gia đình trong một toà nhà có n hộ, biết rằng mỗi hộ gia đình sẽ có thời gian có thể đến lấy chữ ký là khác nhau. Công việc của bạn là phải tối thiểu được số lần đến lấy chữ ký kèm với thời gian đến lấy. Ví dụ hộ A và hộ B đều có thể đến lấy vào thời điểm x như vậy sẽ tiết kiệm công sức hơn khi mỗi hộ sẽ có một thời gian đến lấy khác nhau.
          Mô tả bài toán
    - Nhiệm vụ. Cho một tập hợp n đoạn thời gian {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} trong đó mỗi đoạn thời gian này là 1 khoảng thời gian có mặt ở nhà của mỗi hộ trong n hộ, cụ thể hộ 0 có mặt ở nhà lúc a0 đến lúc b0, hộ 1 có mặt ở nhà lúc a1 đến lúc b1,…, hộ n-1 có nhà lúc an-1 đến lúc bn-1. Mỗi đoạn thời gian chứa ít nhất 1 điểm x. Gọi m là số lượng tối thiểu của thời điểm x sao cho mỗi đoạn thời gian chứa ít nhất 1 điểm x. Hãy tìm m. Hay, tìm tập hợp các số nguyên 𝑋 nhỏ nhất sao cho trên mỗi đoạn [𝑎𝑖, 𝑏𝑖] có một điểm 𝑥 ∈ 𝑋 thỏa mãn 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.
    - Định dạng input. Dòng đầu tiên của input chứa số đoạn n. Mỗi dòng trong n dòng tiếp theo chứa 2 số nguyên ai và bi (được ngăn bởi dấu cách) biểu thị tọa độ hai điểm đầu cuối của đoạn thứ i.
    - Ràng buộc. 1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^9 với mọi 0 ≤ 𝑖 < 𝑛.
    - Định dạng output.  Xuất ra số điểm m tối thiểu trên dòng đầu tiên và tọa độ của m điểm (được ngăn bởi dấu cách) trên dòng thứ hai. Bạn có thể xuất ra các điểm theo thứ tự bất kỳ. Nếu có nhiều tập hợp điểm như vậy, bạn có thể xuất ra một tập hợp bất kỳ. (Không khó để nhận ra rằng luôn luôn tồn tại những tập hợp điểm nhỏ nhất sao cho tất cả các tọa độ của các điểm đều là số nguyên.)
    - Giới hạn thời gian. 5s
    - Giới hạn bộ nhớ. 512MB.
'''
def optimal_points(segments):
    points = []
    #write your code here
    # sắp xếp thời gian hộ gia đình có mặt ở nhà theo thời gian kết thúc
    segments = sorted(segments, key=lambda x: x.end)
    for s in segments:
      # Nếu chưa đi qua điểm nào thì lưu điểm lại theo thời gian kết thúc
      if len(points)==0:
        points.append(s.end)
      # Nếu thời gian bắt đầu điểm đi qua hiện tại sớm hơn điểm lưu trước thì lưu lại điểm mới
      if s.start > points[-1]:
        points.append(s.end)
    return points

if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *data = map(int, input().split())
    # n, data = 3, [1, 3, 2, 5, 3, 6]
    # n, data = 4, [4, 7, 1, 3, 2, 5, 5, 6]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')