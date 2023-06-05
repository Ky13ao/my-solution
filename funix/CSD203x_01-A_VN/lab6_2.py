class SLLNode:
  # Node class for SingleLinkedList class
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
class SingleLinkedList:
  def __init__(self):
    self.head = None
  def push(self, data):
    # insert an node to list object at the bottom
    #  for almost exercise in this lab
    newNode = SLLNode(data)
    if self.head is None:
      self.head = newNode
      return
    node = self.head
    while node.next:
      node = node.next
    node.next = newNode
  def getAt(self, index):
    #get an element at [index] position
    counter = 0
    node = self.head
    while node:
      if counter == index:
        return node
      node = node.next
      counter+=1
  def removeLargerAt(self, index):
    #removes all node with data larger than node at [index]
    #  of the list
    nodeAtIndex = self.getAt(index)
    if not nodeAtIndex:
      return
    value = nodeAtIndex.data
    node = self.head
    preNode = SLLNode(None, node)
    while node:
      if node.data>value:
        preNode.next = node.next
      else:
        if not preNode.data:
          self.head = preNode.next
        preNode.next = node
        preNode = preNode.next
      node = node.next
  def setAtoB(self, a, b):
    #set all node with value a to value b
    node = self.head
    while node:
      if node.data == a:
        node.data = b
      node = node.next
    return self  
  def removeAt(self, index):
    #remove node at [index] position
    if index<0:
      return
    if index == 0:
      return self.shift()
    node = self.getAt(index-1)
    if node is None or node.next is None:
      return
    removin = node.next
    node.next = removin.next
    return removin
  def shift(self):
    #remove head node
    node = self.head
    self.head = node.next
    return node
  def unshift(self, data):
    #insert a node at begin of list
    newNode = SLLNode(data, self.head)
    self.head = newNode
  def insertAt(self, index, data):
    #insert a node at [index] position
    newNode = SLLNode(data)
    if self.head is None:
      self.head = newNode
      return
    if index==0:
      # self.head = Node(data, self.head)
      newNode.next = self.head
      self.head = newNode
      return
    pre = self.getAt(index-1)
    if not pre is None:
      newNode.next = pre.next
      pre.next = newNode
      return self.head
    else:
      self.push(data)
  def __str__(self):
    strOut = ''
    node = self.head
    while node:
      strOut += str(node.data) + ' '
      node = node.next
    return strOut

def singleListLinker(list_in):
  # main proc for 21-31
  list_obj = SingleLinkedList()
  for e in list_in:
    list_obj.push(e)
  return list_obj

def singleListInsertAt(list_in, k, x):
  # main proc for 22
  list_obj = singleListLinker(list_in)
  list_obj.insertAt(k, x)
  return list_obj

def singleListRemoveAt(list_in, k):
  # main proc for 23
  list_obj = singleListLinker(list_in)
  list_obj.removeAt(k)
  return list_obj

def singleListValueAt(list_in, k):
  # main proc for 24
  list_obj = singleListLinker(list_in)
  return list_obj.getAt(k).data

def singleListSetAtoB(list_in, a, b):
  # main proc for 25
  list_obj = singleListLinker(list_in)
  list_obj.setAtoB(a, b)
  return list_obj

def singleListRemoveLargerAt(list_in, k):
  # main proc for 26
  list_obj = singleListLinker(list_in)
  list_obj.removeLargerAt(k)
  return list_obj

class DLLNode:
  # Node class for DoublyLinkedList class
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList():
  def __init__(self, head=None):
    self.head = None
    self.tail = self.head
  def push(self, data):
    newNode = DLLNode(data)
    if not self.head:
      self.head = newNode
      self.tail = newNode
      return self.head
    else:
      self.tail.next = newNode
      newNode.prev = self.tail
      self.tail = newNode
    return self.head
  def getAt(self, index):
    pass
    if index<0:
      return
    if index==0:
      return self.head
    counter=0  
    current = self.head
    while current:
      if counter==index:
        return current
      counter+=1
      current = current.next
  def removeAt(self, index):
    if index<0:
      return
    if index==0:
      return self.shift()
    node = self.getAt(index)
    if not node:
      return
    bef = node.prev
    after = node.next 
    if node.next:
      after.prev = bef
    bef.next = after
    node.next = None
    node.prev = None
    return node
  def shift(self):
    if not self.head:
      return
    node = self.head.next
    node.prev = None
    self.head = node
  def pushAt(self, index, data):
    if index<0:
      return
    if index==0:
      return self.unshift(data)
    newNode = DLLNode(data)
    current = self.getAt(index-1)
    newNode.next = current.next
    current.next = newNode
    newNode.prev = current
  def unshift(self, data):
    newNode = DLLNode(data)
    newNode.next = self.head
    if self.head:
      self.head.prev = newNode
    self.head = newNode
  def __str__(self):
    strOut = ''
    node = self.head
    while node:
      strOut += str(node.data) + ' '
      node = node.next
    return strOut
  def print2ways(self):
    if not self.head:
      print()
      return
    node = self.head
    strOut = str(node.data)
    while node.next:
      node = node.next
      strOut = str(node.data) + ' '+ strOut + ' ' +str(node.data)
    print(strOut)

class CircularLinkedList(SingleLinkedList):
  def __init__(self):
    self.head = None
    self.tail = self.head
    self.size = 0
  def push(self, data):
    newNode = DLLNode(data)
    newNode.next = self.head
    if not self.head:
      self.head = newNode
      self.tail = self.head
      return
    self.tail.next = newNode
    self.tail = newNode
    self.size+=1
  def printAt(self, index):
    if index<0 or index>=self.size:
      return print() 
    node = self.getAt(index)
    strOut = ''
    counter=0
    while counter<=self.size:
      strOut += str(node.data) + ' '
      node = node.next
      counter+=1
    print(strOut)

def doublyListLinker(list_in):
  # main proc for 28-30
  list_obj = DoublyLinkedList()
  for e in list_in:
    list_obj.push(e)
  return list_obj

def doublyListSequence(n):
  # main proc for 27
  list_obj = DoublyLinkedList()
  for i in range(n):
    list_obj.push(i+1)
  return list_obj

def doublyListPushAt(list_in, k, x):
  # main proc for 28
  list_obj = doublyListLinker(list_in)
  list_obj.pushAt(k, x)
  return list_obj

def doublyListRemoveAt(list_in, k):
  # main proc for 29
  list_obj = doublyListLinker(list_in)
  list_obj.removeAt(k)
  return list_obj

def circularListLinker(list_in):
  list_obj = CircularLinkedList()
  for e in list_in:
    list_obj.push(e)
  return list_obj

def printCircularAt(list_in, k):
  list_obj = circularListLinker(list_in)
  list_obj.printAt(k)

#30 https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/816897
printCircularAt([1,2,3,4], 1)
printCircularAt([1,2,3,4,5],3)
printCircularAt([1,2,3],0)

#29
# print(doublyListRemoveAt([int(input()) for _ in range(int(input()))], int(input())))
# print(doublyListRemoveAt([1,2,3,4], 1))
# print(doublyListRemoveAt([1,2,3,4,5], 0))
# print(doublyListRemoveAt([1,2,3], 2))

#28 https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/813530
# print(doublyListPushAt([int(input()) for _ in range(int(input()))], int(input()), int(input())))
# print(doublyListPushAt([1,2,3], 0, 10))
# print(doublyListPushAt([1,2,3], 3, 10))
# print(doublyListPushAt([1,2,3,4], 2, 10))

#27: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/810202
# doublyListSequence(int(input())).print2ways()

#26: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/809803
# print(singleListRemoveLargerAt([int(input()) for _ in range(int(input()))], int(input())))
# print(singleListRemoveLargerAt([1,1,2,2,3,3],2))
# print(singleListRemoveLargerAt([5,4,3,2,1],3))
# print(singleListRemoveLargerAt([1,2,3,2,1],3))

#25: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/809159
# print(singleListSetAtoB([int(input()) for _ in range(int(input()))], int(input()), int(input())))
# print(singleListSetAtoB([1,1,2,2,3,3], 2, 10))

#24: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/809669
# print(singleListValueAt([int(input()) for _ in range(int(input()))], int(input())))
# print(singleListValueAt([1,2,3,4],2))

#23: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/808185
# print(singleListRemoveAt([int(input()) for _ in range(int(input()))], int(input())))
# print(singleListRemoveAt([1,2,3,4], 1))
# print(singleListRemoveAt([1,2,3], 0))
# print(singleListRemoveAt([1,2,3], 2))

#22: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/777654
# print(singleListInsertAt([int(input()) for _ in range(int(input()))], int(input()), int(input())))
# print(singleListInsertAt([1,2,3,4],1,10)) # 1 10 2 3 4
# print(singleListInsertAt([1,2,3],0,4)) # 4 1 2 3
# print(singleListInsertAt([1,2,3],3,100)) # 1 2 3 100

#21: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/805177
# print(singleListLinker([int(input()) for _ in range(int(input())) ]))
# print(singleListLinker([1,2,3]))
# print(singleListLinker([1,2,3,4,5]))
# print(singleListLinker([1,2,3,3,2,1,2,3,4,8,9,5,4,6,8,9,5,45,66]))

