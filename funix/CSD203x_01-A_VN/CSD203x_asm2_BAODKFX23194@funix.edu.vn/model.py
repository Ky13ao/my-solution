class Node:
  #Prepare fields for data of product
  fields = {'ID': str, 'Title': str, 'Quantity': int, 'Price': float}
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
  
  #Function to align value in cell of table row
  def rowInTabular(self, width_of_columns={k: len(k) for k in fields.keys()}):
    row = []
    for colName, value in self.data.items():
      if type(value) == str:
        row.append(f' {value:<{width_of_columns[colName]}} ')
      else:
        row.append(f' {value:>{width_of_columns[colName]}} ')
    return row

  #Clone self to convert node to be the part of stack or queue
  def copy(self):
    return type(self)(self.data)

class MyList:
  def __init__(self):
    self.head = None
    self.tail = self.head
    self.size=0
  # Push new node that created from outside then use this method to link to the tail
  def pushNode(self, new_node):
    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.size+=1
    return self.tail
  # Function return the node with data[ID] = id provided
  def getById(self, id):
    current = self.head
    while current:
      if current.data['ID']==id:
        break
      current = current.next
    return current
  def removeById(self, id):
    node = self.getById(id)
    if not node:
      return
    before = node.prev
    after = node.next
    #Head node does not have prev linked
    if node.prev:
      before.next = after
    else:
      self.head = after
    #Tail node does not have next linked
    if node.next:
      after.prev = before
    else:
      self.tail = before
    self.size-=1
    return node
  # Insertion Sort method sort on data field
  def sort(self):
    if self.size<=1:
      return self
    current = self.head.next
    while current:
      currentData = current.data
      prevNode = current.prev
      # Swap data only
      while prevNode and currentData['ID']<prevNode.data['ID']:
        prevNode.next.data = prevNode.data
        prevNode = prevNode.prev
      if prevNode is None:
        self.head.data = currentData
      else:
        prevNode.next.data = currentData
      current = current.next
    return self
  # Function to return all of ID in linked list
  def listId(self):
    current = self.head
    a = []
    while current:
      a.append(current.data['ID'])
      current = current.next
    return a
