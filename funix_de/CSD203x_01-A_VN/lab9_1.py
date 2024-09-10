# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    # self.n = int(sys.stdin  .readline())
    self.n=5
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    # for i in range(self.n):
    keys = [[4,1,2],[2,3,4],[5,-1,-1],[1,-1,-1],[3,-1,-1]]
    for i, key in enumerate(keys):
      # [a, b, c] = map(int, sys.stdin.readline().split())
      [a, b, c]=key
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def __inOrderTraversal(node):
      if node==-1:
        return
      __inOrderTraversal(self.left[node])
      self.result.append(self.key[node])
      __inOrderTraversal(self.right[node])
    __inOrderTraversal(0)
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def __preOrderTraversal(node):
      if node==-1:
        return
      self.result.append(self.key[node])
      __preOrderTraversal(self.left[node])
      __preOrderTraversal(self.right[node])
    __preOrderTraversal(0)
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def __postOrderTraversal(node):
      if node==-1:
        return
      __postOrderTraversal(self.left[node])
      __postOrderTraversal(self.right[node])
      self.result.append(self.key[node])
    __postOrderTraversal(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()