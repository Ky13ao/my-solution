class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
  def __str__(self):
    return ' '.join(list(map(str, [self.data, self.next, self.prev])))
  
class DoublyList:
  def __init__(self, head=None):
    self.head = head
    self.tail = None
    self.size = 0
  def push(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
      return self.head
    else:
      self.tail.next = newNode
      newNode.prev = self.tail
      self.tail = newNode
    self.size+=1
    return self.head
  def getAt(self, index):
    if index<0 or index>=self.size:
      return None
    counter = 0
    node = self.head
    while counter != index:
      if node:
        node = node.next
      else:
        return node
      counter+=1
    return node
  def unshift(self, data):
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      self.head.prev = newNode
      newNode.next = self.head
      self.head = newNode
    self.size+=1
    return self
  def pushAt(self, index, data):
    if index>self.size:
      return None
    if index==0:
      self.unshift(data)
    elif index==self.size-1:
      self.push(data)
    else:
      newNode = Node(data)
      after = self.getAt(index)
      before = after.prev
      after.prev = newNode
      before.next = newNode
      newNode.next = after
      newNode.prev = before
      self.size+=1
    return self.head
  def pop(self):
    if self.size ==0:
      return
    popped = self.tail
    newTail = popped.prev
    if newTail:
      newTail.next = None
      self.tail.prev = None
    else:
      self.head = None
    self.tail = newTail
    self.size-=1
    return popped
  def shift(self):
    if self.head is None:
      return
    shiftedNode = self.head
    newHead = self.head.next
    if self.head!=self.tail:
      newHead.prev = None
      shiftedNode.next = None
    else:
      self.tail = None
    self.head = newHead
    self.size-=1
    return shiftedNode
  def removeAt(self, index):
    if index<0 or index>self.size:
      return
    if index==0:
      return self.shift()
    if index==self.size:
      return self.pop()
    removedNode = self.getAt(index)
    after = removedNode.next
    before = removedNode.prev
    removedNode.next = None
    removedNode.prev = None
    before.next = after
    after.prev = before
    self.size-=1
    return removedNode
  def __str__(self):
    if self.head is None:
      return ''
    node = self.head
    strOut = str(node.data)
    while not node.next is None:
      node = node.next
      strOut = str(node.data) + ' ' + strOut + ' ' + str(node.data)
    return strOut.strip()
  def print28(self):
    strOut = ''
    if self.head is None:
      print(strOut)
      return strOut
    node = self.head
    while node:
      strOut += str(node.data) + ' '
      node = node.next
    print(strOut)
    return strOut

def listSequencePusher(n):
  #27 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/810202
  list_obj = DoublyList()
  for i in range(n):
    list_obj.push(i+1)
  return list_obj

def printListPushAt(list_in, k, x):
  #28: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/813530
  list_obj = listLinker(list_in)
  list_obj.pushAt(k, x)
  # print(list_obj.size)
  list_obj.print28()

def printListRemoveAt(list_in, k):
  #29: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/816003
  list_obj = listLinker(list_in)
  list_obj.removeAt(k)
  # print(list_obj)
  list_obj.print28()

def printLinker30(list_in, k):
  #30: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/816897
  list_obj = DoublyList()
  for i in range(k, len(list_in)):
    list_obj.push(list_in[i])
  for i in range(k):
    list_obj.push(list_in[i])
  list_obj.print28()

def listLinker(list_in):
  # 21 : https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/805177
  list_obj = DoublyList()
  for e in list_in:
    list_obj.push(e)
    # print(list_obj.size)
  # print(list_obj)
  return list_obj

# print(listPushAt([int(input()) for _ in range(int(input())) ], int(input()), int(input())))
printLinker30([1,2,3,4],1)
printLinker30([1,2,3,4,5],3)
printLinker30([1,2,3],0)
# printListPushAt([1,2,3],0,10)
# printListPushAt([1,2,3],3,10)
# print(listSequencePusher(int(input())))
# print(listRemoveBigger([int(input()) for _ in range(int(input())) ], int(input())))
# print(listSetAtt([int(input()) for _ in range(int(input())) ], int(input()), int(input())))

# listGetAt([int(input()) for _ in range(int(input())) ], int(input()))

# print(listRemoveAt([int(input()) for _ in range(int(input())) ], int(input())))
# listInsertAt([int(input()) for _ in range(int(input())) ], int(input()), int(input()))
# listLinker([int(input()) for _ in range(int(input())) ])
# listLinker([1,2,3])
