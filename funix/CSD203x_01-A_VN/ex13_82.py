def graphFunction(city_count, streets, start, target):
  adjacency = [[] for _ in range(city_count + 1)]
  visited = [False] * (city_count + 1)
  # Build the adjacency list
  for street in streets:
    x, y = street
    if x > city_count or y > city_count:
      return -1
    adjacency[x].append(y)
    adjacency[y].append(x)

  def dfs(city, distance):
    visited[city] = True

    if city == target:
      return distance

    for neighbor in adjacency[city]:
      if not visited[neighbor]:
        result = dfs(neighbor, distance + 1)
        if result != -1:
          return result

    return -1

  return dfs(start, 1)

# Example usage:
n = 6
a = [[1, 3], [1, 2], [2, 3], [3, 4], [2, 5], [4, 6], [6, 5], [4, 5]]
u = 1
v = 5

print(graphFunction(n, a, u, v))  # Output: 4

n = 2
a = [[1, 2], [3, 4]]
u = 2
v = 3

print(graphFunction(n, a, u, v))  # Output: -1

n, a, u, v = 6,[[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]],1,6
print(graphFunction(n, a, u, v))  # Output: 5
