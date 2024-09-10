
class Tree():
  def search(self, value):
    node = self.head
    while node:
      if node.data == value:
        return 1
      if value<node.data:
        node = node.left
      else:
        node = node.right
    return -1
  def search2(self, value):
    return searchsupport(self.head, value)

def value_of(start, target):
  if start==target:
    return start
  else:
    for neighbor in start.neightbors:
      return value_of(start.neightbor, target)

def searchsupport(node, value):
  if not node:
    return -1
  if node.data == value:
    return 1
  if value<node.data:
    return searchSupport(node.left, value)
  else:
    return searchSupport(node.right,value)


if __name__ == "__main__":
  main()