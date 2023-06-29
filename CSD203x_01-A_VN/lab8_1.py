# Lab 8.1: https://drive.google.com/file/d/1DmTef4OgAu5xo7Usl2KRh0tbNJdGif4h/view

''' Giới thiệu bài toán
Cây được sử dụng để thao tác với dữ liệu phân cấp chẳng hạn như hệ thống phân cấp các danh mục của một nhà bán lẻ hoặc cấu trúc thư mục trên máy tính của bạn. Chúng cũng được sử dụng trong phân tích dữ liệu và học máy cho cả phân cụm thứ bậc và xây dựng các mô hình dự đoán phức tạp, bao gồm một số thuật toán hoạt động tốt nhất trong thực tế như Gradient Boosting trên Decision Trees (cây quyết định) và Random Forests (Rừng ngẫu nhiên). Trong các học phần sau của khóa học này, chúng tôi sẽ giới thiệu Cây tìm kiếm nhị phân cân bằng (BST) - một loại cây đặc biệt cho phép lưu trữ, thao tác và truy xuất dữ liệu rất hiệu quả. Do đó, các BST cân bằng được sử dụng trong cơ sở dữ liệu để lưu trữ hiệu quả và trong hầu hết các chương trình không tầm thường nữa, thường là thông qua cấu trúc dữ liệu tích hợp sẵn của ngôn ngữ lập trình.
Trong bài toán này, mục tiêu của bạn là làm quen với cây. Bạn sẽ cần đọc mô tả cây từ input, triển khai cấu trúc dữ liệu cây, lưu trữ cây và tính chiều cao của nó.
    Mô tả bài toán
Nhiệm vụ. Bạn được cung cấp mô tả về một cây có gốc. Nhiệm vụ của bạn là tính và xuất ra chiều cao của nó. Nhớ rằng chiều cao của cây (có gốc) là độ sâu tối đa của một node (nút), hoặc khoảng cách tối đa từ lá đến gốc. Bạn được cung cấp một cây bất kỳ, không nhất thiết phải là một cây nhị phân.
Định dạng input:
- Dòng đầu tiên chứa số đỉnh 𝑛.
- Dòng thứ hai chứa 𝑛 số nguyên từ −1 đến 𝑛 − 1 - parent (cha) của các đỉnh.
   Nếu đỉnh thứ i trong số chúng (0 ≤ 𝑖 ≤ 𝑛 - 1) là −1, thì đỉnh 𝑖 là gốc, nếu không thì nó là index bắt đầu từ 0 của parent của đỉnh thứ 𝑖. Đảm bảo rằng chỉ có một gốc. Đảm bảo rằng input biểu diễn một cây.
- Ràng buộc. 1 ≤ 𝑛 ≤ 10^5.
Định dạng output: Xuất ra chiều cao của cây.
Giới hạn thời gian: 5s
Giới hạn bộ nhớ: 512Mb.
'''
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
  def read(self):
    # self.n = int(sys.stdin.readline())
    # self.parent = list(map(int, sys.stdin.readline().split()))
    self.n = 5
    # self.parent = [4, -1, 4, 1, 1]
    self.parent = [-1, 0, 4, 0, 3]

  def compute_height_origin(self):
    # Replace this code with a faster implementation
    maxHeight = 0
    for vertex in range(self.n):
      height = 0
      i = vertex
      while i != -1:
        height += 1
        i = self.parent[i]
      maxHeight = max(maxHeight, height);
    return maxHeight;
  
  def compute_height(self):
    # Optimize the origin method
    heights = {}
    def calculate_height(vertex):
      if vertex==-1:
        return 0
      # nếu đã ghi đỉnh này vào height thì trả về giá trị đã ghi
      if vertex in heights:
        return heights[vertex]
      # nếu chưa ghi đỉnh cha của đỉnh này thì tính chiều cao đỉnh cha bằng phương pháp đệ quy
      if self.parent[vertex] not in heights:
        heights[self.parent[vertex]] = calculate_height(self.parent[vertex])
      # chiều cao của đỉnh sẽ bằng chiều cao của đỉnh cha + 1
      height = heights[self.parent[vertex]] + 1
      heights[vertex] = height
      # trả giá trị cho đệ quy
      return height
    # tìm ra chiều cao cao nhất của các đỉnh bằng cách ghi lại vào dict những giá trị đã tính
    return max(calculate_height(vertex) for vertex in range(self.n))

def main():
  import time
  tree = TreeHeight()
  tree.read()
  start2=time.time()
  print(tree.compute_height())
  end2=time.time()
  print("optimize execution time", end2-start2)
  start1=time.time()
  print(tree.compute_height_origin())
  end1=time.time()
  print("origin execution time", end1-start1)

threading.Thread(target=main).start()