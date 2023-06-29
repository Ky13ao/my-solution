# codelearn.io 62-69

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

# Compare the new value with the parent node
  def insert(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.insert(data)
      else:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data

# Function to check a node is leaf or not
  def isLeafNode(self, node):
    return (node.left is None and node.right is None)

  def countLeafNode(self, node):
    if node is None:
      return 0
    if self.isLeafNode(node):
      return 1
    return self.countLeafNode(node.left)+self.countLeafNode(node.right)
    

# Print the tree
  def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print( self.data, end=' '),
    if self.right:
      self.right.PrintTree()

# Use the insert method to add nodes
def bstInsert(list_in):
  root = Node(list_in[0])
  for n in list_in[1:]:
    root.insert(n)
  return root

if __name__=='__main__':
  # Create a binary search tree
  # bst = bstInsert(list(map(int, [input() for _ in range(int(input()))])))
  # bst = bstInsert([1,2,3,3,2,1])
  bst = bstInsert([4, 7, 2, 1, 3, 2, 5])
  print(bst.countLeafNode(bst))
  # bst.PrintTree()