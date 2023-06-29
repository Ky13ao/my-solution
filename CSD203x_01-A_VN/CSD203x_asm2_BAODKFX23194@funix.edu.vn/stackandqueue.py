from model import Node

class MyStack:
  def __init__(self):
    self.stack = []
    self.width_of_columns = {key:len(key) for key in Node(None).fields.keys() }
  def pushFromLL(self, linked_list):
    if linked_list.head == None:
      return
    node = linked_list.head
    while node:
      stackNode = node.copy()
      self.stack.insert(0, stackNode)
      self.updateWidthOfColumns(stackNode.data)
      node = node.next
  def updateWidthOfColumns(self, data):
    for colName, size in self.width_of_columns.items():
      if len(str(data[colName])) > size:
        self.width_of_columns[colName] = len(str(data[colName]))
  def __str__(self):
    if len(self.stack)==0:
      return 'Nothing data in dataset!'
    strOutLines = ['|'.join(f' {k:^{self.width_of_columns[k]}} ' for k in self.stack[0].fields.keys())]
    for node in self.stack:
      strOutLines.append('|'.join(node.rowInTabular(self.width_of_columns)))
    return '\n'.join(strOutLines)

class MyQueue:
  def __init__(self):
    self.queue = []
    self.width_of_columns = {key:len(key) for key in Node(None).fields.keys() }
  def pushFromLL(self, linked_list):
    if linked_list.head == None:
      return
    node = linked_list.head
    while node:
      queueNode = node.copy()
      self.queue.append(queueNode)
      self.updateWidthOfColumns(queueNode.data)
      node = node.next
  def updateWidthOfColumns(self, data):
    for colName, size in self.width_of_columns.items():
      if len(str(data[colName])) > size:
        self.width_of_columns[colName] = len(str(data[colName]))
  def __str__(self):
    if len(self.queue)==0:
      return 'Nothing data in dataset!'
    strOutLines = ['|'.join(f' {k:^{self.width_of_columns[k]}} ' for k in self.queue[0].fields.keys())]
    for node in self.queue:
      strOutLines.append('|'.join(node.rowInTabular(self.width_of_columns)))
    return '\n'.join(strOutLines)
