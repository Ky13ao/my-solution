"""
Cho một đồ thị có hướng với n đỉnh, các đỉnh được đánh số từ 1 tới n. Hãy viết hàm kiểm tra xem có tồn tại đường đi từ đỉnh u tới đỉnh v (u khác v) hay không?
Các cạnh của đồ thị được biểu diễn dưới dạng mảng 2 chiều. Ví dụ:
e = [[1, 2], [2, 3]] có nghĩa là có cạnh nối giữa đỉnh 1 và đỉnh 2, đỉnh 2 và đỉnh 3.
Ví dụ
    Cho n = 3, e = [[1, 2], [2, 3]], u = 1, v = 3, output sẽ có dạng findPath(n, e, u, v) = true. Giải thích: đường đi từ đỉnh 1 tới đỉnh 3 có dạng: 1 -> 2 -> 3.
    Cho n = 4, e = [[1, 2], [3, 4], [2, 4]], u = 1, v = 3, output sẽ có dạng findPath(n, e, u, v) = false. Giải thích: Từ đỉnh 3 chỉ có cạnh đi ra chứ không có cạnh đi vào nên không có đỉnh nào có thể đi tới được đỉnh 3.
"""

def check(n, e, u, v):
  # giả thiết các đỉnh đều được đi qua
  visited = [True] * (n + 1)
  # và n+1 cạnh ko đi qua
  adjacency = [[False] * (n + 1) for _ in range(n + 1)]
  for edge in e:
    # các cạnh được nêu trong input đều sẽ được đi qua
    adjacency[edge[0]][edge[1]] = True
  
  def dfs(start, target, nodes_count, adjacency, visited):
    # thủ tục dfs duyệt các đỉnh theo chiều sâu
    # đỉnh duyệt sẽ không duyệt lại
    visited[start]=False
    for i in range(1, nodes_count+1):
      if adjacency[start][i] and visited[i]:
        # khi duyệt hết các đỉnh, dừng duyệt
        if i == target:
          return True
        # duyệt đỉnh có cạnh liền kề
        if dfs(i, target, nodes_count, adjacency, visited):
          return True
        # đánh dấu đã duyệt
        visited[i]=True
    return False
  return dfs(u, v, n, adjacency, visited)

# n, e, u, v = 3, [[1, 2], [2, 3]], 1, 3
n, e, u, v = 4,[[1,2],[3,4]],1,3
print(check(n, e, u, v))