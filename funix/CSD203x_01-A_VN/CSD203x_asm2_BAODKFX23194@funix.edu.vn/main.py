from model import Node, MyList
from operation import OperationToProduct
from stackandqueue import MyStack, MyQueue

class AS2_Main:
  def __init__(self):
    self.ops = OperationToProduct()
    self.menuItems = [{"context":"Load data from file and display", "command": self.readPathForLoading},
                {"context":"Input & add to the end", "command": self.pushFromInput},
                {"context":"Display data", "command": lambda: print(self.ops)},
                {"context":"Save product list to file.", "command": self.readPathForSaving},
                {"context":"Search by ID", "command": self.readIdForSearching},
                {"context":"Delete by ID", "command": self.readIdForDeleting},
                {"context":"Sort by ID", "command": self.ops.sortById},
                {"context":"Convert to Binary", "command": self.readIdForConverting},
                {"context":"Load to stack and display", "command": self.loadListToStackAndDisplay},
                {"context":"Load to queue and display", "command": self.loadListToQueueAndDisplay}
                ]
  def loadListToQueueAndDisplay(self):
    queue = MyQueue()
    queue.pushFromLL(self.ops)
    print(queue)
  def loadListToStackAndDisplay(self):
    stack = MyStack()
    stack.pushFromLL(self.ops)
    print(stack)
  def pushFromInput(self):
    data = {}
    newNode = Node(data)
    for field in newNode.fields.keys():
      tooltip = 'Please enter '
      if field == 'ID':
        tooltip += 'new product ID: '
        while True:
          fieldValue = input(tooltip).upper()
          listId = self.ops.listId()
          if fieldValue in listId:
            print('ID already in use.')
            continue
          break
        data[field] = fieldValue
      else:
        tooltip += "product's %s: " % field.lower()
        while True:
          try:
            fieldValue = newNode.fields[field](input(tooltip))
          except ValueError:
            print('Invalid input')
            continue
          break
        data[field] = fieldValue
        newNode.data = data
    self.ops.pushNode(newNode)
  def readPathForLoading(self):
    filePath = input("Please enter the file path: ")
    self.ops.loadListFromTSVFile(filePath)
  def readPathForSaving(self):
    filePath = input("Please enter the output path: ")
    self.ops.saveListToTSVFile(filePath)
  def readIdForDeleting(self):
    id = input('Please enter the ID: ')
    self.ops.deleteProductById(id)
  def readIdForSearching(self):
    id = input('Please enter the ID: ')
    self.ops.searchById(id)
  # Câu 8 Trong hướng dẫn có nêu nhập ID, nhưng trong tiêu chí nói rõ là convert phần từ đầu tiên
  def readIdForConverting(self):
    # Bỏ trống input để chạy theo tiêu chí
    id = input('Please enter the ID: (Leaves blank will return head of list) ').strip()
    # Chương trình sẽ chạy theo hướng dẫn nếu độ dài input>0
    node = self.ops.getById(id.upper()) if len(id)>0 else self.ops.head
    self.ops.convertQtyToBinary(node)
  def launch(self):
    while True:
      print('+-----------------------------+')
      maxkeyLen = len(str(len(self.menuItems)))
      print('\n'.join([f'{i+1: >{maxkeyLen}}. {_["context"]}' for i, _ in enumerate(self.menuItems)]))
      print('Exit:\n0. Exit')
      optStdIn = input('[>] Input key menu you wish to run: ').strip()
      try:
        opt = int(optStdIn)
      except:
        print('Invalid option. Try again')
        continue
      if int(opt)<0 or opt>len(self.menuItems):
        # Kiểm tra lựa chọn có trong menu
        print('[!] Invalid key menu. Try again')
      else:
        # Sau khi kiểm tra tất cả các dữ liệu cần thiết, tiến hành Chạy command đã chọn
        if opt!=0:
          print('[✔] Choice %s: %s' % (opt, self.menuItems[opt-1]['context'] ))
          arrThru = self.menuItems[opt-1]['command']()
        else:
          print('Thanks!!!')
          break
    print('+-----------------------------+')

if __name__ == "__main__":
  app = AS2_Main()
  # data for trial run from beginning
  app.ops.loadListFromTSVFile("outdata.txt")
  app.launch()