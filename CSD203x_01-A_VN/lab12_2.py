#Uses python3

import sys


def number_of_components(adj):
  result = 0
  #write your code here
  visited = [False] * len(adj)

  def explore(vertex):
    visited[vertex]=True #mark the current vertex as visited
    for neightbor in adj[vertex]:
      if not visited[neightbor]:
        explore(neightbor) #recursive explore neightbor if not yet visited

  for v in range(len(adj)):
    if not visited[v]:
      explore(v)
      result+=1
    
  return result

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
  print(number_of_components(adj))