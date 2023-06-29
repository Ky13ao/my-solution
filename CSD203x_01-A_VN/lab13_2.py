import sys
from queue import Queue

def bipartite(adj):
  #write your code here  
  color = [None] * len(adj) #Lập mảng rỗng có độ dài bằng độ dài cách cạnh

  def bfs(source):
    # tô màu 0 cho đỉnh gốc
    color[source] = 0
    # lập hàng chờ và đưa đỉnh gốc vào trước
    queue = Queue()
    queue.put(source)

    # Duyệt hàng chờ
    while not queue.empty():
      u = queue.get()
      # Duyệt các cạnh có đỉnh là u, u là đỉnh vừa lấy ra trong hàng đợi, uv là các cạnh đang duyệt
      for v in adj[u]:
        # nếu đỉnh v ko có màu thì:
        #   tô màu: màu đỉnh v sẽ ngược lại màu đỉnh u
        #   đưa đỉnh v vào hàng đợi
        # nếu màu đỉnh v = màu đỉnh u thì trả về 0
        if color[v] is None:
          color[v] = 1 - color[u]
          queue.put(v)
        elif color[v] == color[u]:
          return 0
    
    return 1

  for v in range(len(adj)):
    # Nếu đỉnh chưa tô màu
    # ta kiểm đồ thị từ đỉnh `v` không lưỡng phân thì trả về 0
    if color[v] is None:
      if not bfs(v):
        return 0

  return 1
  # return -1

if __name__ == '__main__':
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n, m = data[0:2]
  data = data[2:]
  edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
  adj = [[] for _ in range(n)]
  for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
  print(bipartite(adj))