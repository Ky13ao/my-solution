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
  queue = deque([(start_city, 0)])
  visited = [False] * (num_cities + 1)
  visited[start_city] = True

  while queue:
    current_city, distance = queue.popleft()
    if current_city == target_city:
      return distance
    for neighbor in adjacency[current_city]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append((neighbor, distance + 1))

  return -1

# n, e, u, v =6,[[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]],1,5
# n, e, u, v =6,[[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]],2,3
n, e, u, v =4,[[1,2],[3,4]],2,3
print(shortest_distance(n, e, u, v))