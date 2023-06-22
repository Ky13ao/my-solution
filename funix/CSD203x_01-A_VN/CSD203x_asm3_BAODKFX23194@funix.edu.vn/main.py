from queue import MyQueue
from model import MyPerson, PeopleBSTree
from msvcrt import getch

class Main:
  def __init__(self):
    # Tạo cây BST và hàng đợi riêng biệt để dễ control hơn
    self.BST = PeopleBSTree()
    self.queue = MyQueue()
    # Đặt đường dẫn file data mặc định là data.tsv
    self.datafile = "data.tsv"
    self.menuItems = [{"context":"Load the data from the file", "command": self.readPathForLoading},
                {"context":"Insert a new Person", "command": self.addPerson},
                {"context":"Inorder traverse", "command": self.inOrderTraversal},
                {"context":"Breadth-First Traversal traverse", "command": self.breadthFirstTraversal},
                {"context":"Search by Person ID", "command": self.searching},
                {"context":"Delete by Person ID", "command": self.removing},
                ]

  def readPathForLoading(self):
    # Yêu cầu nhập đường dẫn file cho đến khi mở được file
    while True:
      filePath = input("Please enter the file path: ")
      try:
        file = open(filePath, "r")
      except FileNotFoundError:
        print("File path is invalid!")
        continue
      break
    # Cập nhật đường dẫn file cho file data
    self.datafile = filePath
    # Đọc và thêm nhân viên theo từng dòng trong file
    lines = file.read().split('\n')
    for line in lines:
      if len(line) == 0 or "#" in line[0]:
        continue
      row = line.strip("\t").split("\t")
      newNode = self.BST.insert(MyPerson(row.pop(0)))
      if newNode[1]!=2:
        newPerson = newNode[0].person
        newPerson.update(dict(zip(newPerson.fields[1:], row)))
    print("The file is loaded successfully!")

  def addPerson(self):
    while True:
      personId = input("New ID: ")
      newNode = self.BST.insert(MyPerson(personId))
      if newNode[1] == 2:
        print("This ID has been chosen, please choose another ID!")
        continue
      break
    person = newNode[0].person
    for f in person.fields[1:]:
      person.info[f] = input(f"{f}: ").strip()
    person.saveToFile(self.datafile)

  def inOrderTraversal(self):
    if self.BST.root is None:
      print("Empty `Tree`. Please add a person!")
      return
    self.BST.inOrderQueue(self.queue)
    print(self.queue)

  def breadthFirstTraversal(self):
    if self.BST.root is None:
      print("Empty `Tree`. Please add a person!")
      return
    self.BST.breadthFirstQueue(self.queue)
    print(self.queue)

  def searching(self):
    if self.BST.root is None:
      print("Empty `Tree`. Please add a person!")
      return
    personId = input("Search for ID = ")
    # Thêm kết qua tìm kiếm vào hàng đợi để in
    self.queue.enqueue(self.BST.search(personId).person)
    print(self.queue)

  def removing(self):
    if self.BST.root is None:
      print("Empty `Tree`. Please add a person!")
      return
    personId = input("Delete the person with ID = ")
    # Lưu nhân viên đã bị loại trừ vào biến tạm
    removedPerson = self.BST.delete(personId).person
    # Thêm vào hàng đợi để in
    self.queue.enqueue(removedPerson)
    print(self.queue)
    # Loại bỏ nhân viên trong file data
    removedPerson.removeInFile(self.datafile)

  def launch(self):
    while True:
      print('+------------------Menu--------------------+')
      maxkeyLen = len(str(len(self.menuItems)))
      print('\n'.join([f'     {i+1: >{maxkeyLen}}. {_["context"]}' for i, _ in enumerate(self.menuItems)]))
      print(' '*5+'Exit:\n'+' '*5 +'0. Exit')
      print('+-----------------------------------------.+')
      optStdIn = input('[>] Input your selection: ').strip()
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
          print('Type anything to come back to main menu',end="")
          # Phương thức cho phép chương trình chờ user nhập 1 phím bất kỳ 
          getch()
          print('')
        else:
          print('Thanks!!!')
          break

if __name__ == "__main__":
  app = Main()
  app.launch()

  