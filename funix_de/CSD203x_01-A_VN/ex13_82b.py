def graphFunction(city_count, streets, start, target):
  visited = [True] * (city_count + 1)
  adjacency = [[False] * (city_count + 1) for _ in range(city_count + 1)]
  longestDistance = -1

  def dfs(current_city, distance):
    nonlocal longestDistance
    visited[current_city] = False

    for nextCity in range(1, city_count + 1):
      if adjacency[current_city][nextCity] and visited[nextCity]:
        if nextCity == target and distance + 1 > longestDistance:
          longestDistance = distance + 1
          break
        dfs(nextCity, distance + 1)
        visited[nextCity] = True

  for i in range(len(streets)):
    x, y = streets[i]
    if x>city_count or y>city_count:
      return -1
    adjacency[x][y] = True
    adjacency[y][x] = True

  dfs(start, 0)
  return longestDistance


# Example usage:
n = 6
a = [[1, 3], [1, 2], [2, 3], [3, 4], [2, 5], [4, 6], [6, 5], [4, 5]]
u = 1
v = 5

print(graphFunction(n, a, u, v)) # Output: 4

n = 2
a = [[1, 2], [3, 4]]
u = 2
v = 3

print(graphFunction(n, a, u, v)) # Output: -1

n, a, u, v = 6,[[1,3], [1,2], [2, 3], [3,4], [2,5], [4,6], [6,5], [4,5]],1,6
print(graphFunction(n, a, u, v)) # Output: 5

city_count = 5
streets = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]
start = 1
target = 5

print(graphFunction(city_count, streets, start, target)) # Output: 4