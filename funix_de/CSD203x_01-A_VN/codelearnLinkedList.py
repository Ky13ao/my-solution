class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  def __str__(self):
    return ' '.join(list(map(str, [self.data, self.next])))
  
class LinkedList:
  def __init__(self, head=None):
    self.head = head
    self.tail = None
    self.length = 1
  def push(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      self.tail = self.head
      return self.head
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length+=1
    return self
  def getAt(self, index):
    if index<0 or index>=self.length:
      return None
    counter = 0
    node = self.head
    while counter != index:
      node = node.next
      counter+=1
    return node
  def removeBigger(self, k):
    nodeAtK = self.getAt(k)
    if nodeAtK is None:
      return self
    value = nodeAtK.data
    if self.head is None:
        return None
    node = self.head
    while node.next is not None:
      if node.next.data > value and node.next.next is not None:
        temp = node.next
        node.next = temp.next
        continue
      node = node.next
    if self.head.data > value:
        self.shift()
    if node.data > value:
        self.pop()
    return self
  def pushAt(self, index, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      return
    if index==0:
      self.head = Node(data, self.head)
      return
    pre = self.getAt(index-1)
    if not pre is None:
      newNode.next = pre.next
      pre.next = newNode
      return self.head
    else:
      self.push(data)
  def clear(self):
    if self.head is None:
      return
    self.head = None
    self.tail = None
    self.length = 0
  def pop(self):
    if self.head is None:
      return
    node = self.head
    while not node.next.next is None:
      node = node.next
    self.tail = node
    self.tail.next = None
    self.length-=1
    if self.length==0:
      self.clear()
    return node
  def shift(self):
    if self.head is None:
      return
    headNode = self.head
    self.head = headNode.next
    self.length-=1
    return headNode
  def removeAt(self, index):
    if index<0 or index>=self.length:
      return
    if index==0:
      return self.shift()
    if index==self.length-1:
      return self.pop()
    preNode = self.getAt(index-1)
    removedNode = preNode.next
    preNode.next = removedNode.next
    self.length-=1
    return removedNode
  def setAll(self, old_data, new_data):
    node = self.head
    while not node is None:
      if node.data == old_data:
        node.data = new_data
      node = node.next
  def __str__(self):
    strOut = ''
    node = self.head
    while not node is None:
      strOut += str(node.data) + ' '
      node = node.next
    return strOut

def listLinker(list_in):
  # 21 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/805177
  list_obj = LinkedList()
  for e in list_in:
    list_obj.push(e)
  # print(list_obj)
  return list_obj

def listRemoveBigger(list_in, k):
  # 26 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/809803
  list_obj = listLinker(list_in)
  print(list_obj, k)
  return list_obj.removeBigger(k)

def listInsertAt(list_in, k, x):
  # 22 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/777654
  list_obj = listLinker(list_in)
  list_obj.pushAt(k, x)
  list_obj.printOut()

def listRemoveAt(list_in, k):
  # 23 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/808185
  list_obj = listLinker(list_in)
  list_obj.removeAt(k)
  return list_obj

def listGetAt(list_in, k):
  # 24 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/809669
  list_obj = listLinker(list_in)
  print(list_obj.getAt(k).data)

def listSetAtt(list_in, a, b):
  # 25 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/809159
  list_obj = listLinker(list_in)
  list_obj.setAll(a, b)
  return list_obj

# print(listRemoveBigger([int(input()) for _ in range(int(input())) ], int(input())))
print(listRemoveBigger([1,1,2,2,3,3],2))
print(listRemoveBigger([5,4,3,2,1],3))
print(listRemoveBigger([1,2,3,2,1],3))
# print(listSetAtt([int(input()) for _ in range(int(input())) ], int(input()), int(input())))

# listGetAt([int(input()) for _ in range(int(input())) ], int(input()))

# print(listRemoveAt([int(input()) for _ in range(int(input())) ], int(input())))
# listInsertAt([int(input()) for _ in range(int(input())) ], int(input()), int(input()))
# listLinker([int(input()) for _ in range(int(input())) ])
# listLinker([1,2,3])
