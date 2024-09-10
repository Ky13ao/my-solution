from collections import deque

def shortest_distance(num_cities, edges, start_city, target_city):
  # Create adjacency list
  adjacency = [[] for _ in range(num_cities + 1)]

  # Build the adjacency list
  for edge in edges:
    u, v = edge
    adjacency[u].append(v)
    adjacency[v].append(u)

  # Perform breadth-first search
  # cho lịch trình đi qua các đỉnh vào queue
  queue = deque([(start_city, 0)])
  # giả thiết cho tất cả các đỉnh đều chưa qua
  visited = [False] * (num_cities + 1)
  # đỉnh hiện tại sẽ được đánh dấu đã đi qua
  visited[start_city] = True

  while queue:
    # thăm đỉnh đầu hàng chờ
    current_city, distance = queue.popleft()
    if current_city == target_city:
      # nếu đỉnh hiện tại là đỉnh cuối thì trả về khoảng cách giữa 2 điểm 
      return distance
    for neighbor in adjacency[current_city]:
      if not visited[neighbor]:
        # nếu đỉnh liền kề chưa duyệt
        # đánh dấu duyệt và thêm vào cuối hàng chờ, tăng khoảng cách lên 1
        visited[neighbor] = True
        queue.append((neighbor, distance + 1))

  return -1

# n, e, u, v =6,[[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]],1,5
# n, e, u, v =6,[[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]],2,3
n, e, u, v =4,[[1,2],[3,4]],2,3
print(shortest_distance(n, e, u, v))