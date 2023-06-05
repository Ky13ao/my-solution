from model import Node, MyList

class OperationToProduct(MyList):
  def __init__(self):
    super().__init__()
    self.width_of_columns = {key:len(key) for key in Node(None).fields.keys() }
  def pushNode(self, new_node):
    self.updateWidthOfColumns(new_node.data)
    super().pushNode(new_node)
  def updateWidthOfColumns(self, data):
    for colName, size in self.width_of_columns.items():
      if len(str(data[colName])) > size:
        self.width_of_columns[colName] = len(str(data[colName]))
  def searchById(self, id):
    node = self.getById(id.upper())
    if node:
      print(self.__str__(node))
    else:
      print('ID is not in the dataset!')
  def convertQtyToBinary(self, node):
    # Child recursive function return base 2 from base 10
    def binaryOf(num):
      if num<=1:
        return '%d' % num
      return binaryOf(num//2) + '%d' % (num%2)
    if node:
      print(self.__str__(node))
      print('Convert quantity to binary :', binaryOf(node.data['Quantity']))
    else:
      print('ID is not in the dataset!')
  # Call sort method of the list then display self
  def sortById(self):
    print(self.sort())
  def deleteProductById(self, id):
    product = self.removeById(id.upper())
    if not product:
      print('ID is not in the dataset!')
    else:
      print(self.__str__(product))
      print('The product is removed from the data set successfully!')
  # Đề không nêu rõ định dạng của file input nên mình viết theo format TSV
  def loadListFromTSVFile(self, file_path):
    try:
      f = open(file_path, "r")
      content = f.read()
      f.close()
    except Exception:
      print("File path is not correct!")
      return
    self.parseTSV(content)
    print("The file is loaded successfully!")
  # Method to save list to TSV file
  def saveListToTSVFile(self, file_path):
    try:
      content = self.tsv()
      f = open(file_path, "w")
      f.write(content)
      f.close()
    except Exception:
      print("Error saving to file.")
      return
    print("The file is saved successfully!")
  # Function to prepare TSV data before saving
  def tsv(self):
    if self.head is None:
      return '\t'.join(self.width_of_columns.keys())
    current = self.head
    strOutLines=['\t'.join(current.fields.keys())]
    while current:
      strOutLines.append('\t'.join(list(map(str, current.data.values()))))
      current = current.next
    return '\n'.join(strOutLines)
  # Method to parse TSV data from TSV file loads
  def parseTSV(self, tsv_content):
    typeOfFields = Node(None).fields
    listId = self.listId()
    lines = tsv_content.split('\n')
    headers = lines[0].split('\t')
    for line in lines[1:]:
      row = line.split('\t')
      newNode = Node(None)
      data = {header: newNode.fields[header](value) for header,value in zip(headers, row)}
      if data['ID'] in listId:
        print('ID is not unique!')
        return
      newNode.data = data
      self.pushNode(newNode)
  def __str__(self, node=None):
    if self.head is None:
      return 'Nothing data in dataset!'
    strOutLines = ['|'.join(f' {k:^{self.width_of_columns[k]}} ' for k in self.head.fields.keys())]
    is1Row=False
    if node:
      is1Row=True
    else:
      node = self.head
    while node:
      strOutLines.append('|'.join(node.rowInTabular(self.width_of_columns)))
      if is1Row: 
        break
      node = node.next
    return '\n'.join(strOutLines)
  
