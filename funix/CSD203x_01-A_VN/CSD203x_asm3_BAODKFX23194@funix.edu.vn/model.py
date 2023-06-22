class Person:
  def __init__(self, id):
    self.id = id
    self.info = {}
  def removeInFile(self, file_path):
    lines = open(file_path, 'r').readlines()
    with open(file_path, 'w') as file:
      for line in lines:
        if len(line)==0:
          continue
        id = line.strip('\t').split('\t')[0]
        if id!=self.id:
          file.write(line)


class MyPerson(Person):
  fields = ["ID", "Name", "Day of Birth", "Birthplace"]
  # Phương thức cập nhật thông tin của nhân viên ngoại trừ ID
  def update(self, person):
    self.info = person

  # Dùng __iter__ để xuất object theo dạng dict
  def __iter__(self):
    for f in self.fields:
      if f=="ID":
        yield f, self.id
      else:
        yield f, self.info[f]

  def saveToFile(self, file_path_where_save):
    with open(file_path_where_save,"a") as f:
      f.write('\t'.join(dict(self).values()) + '\n')


class Node:
  def __init__(self, person=None):
    self.person = person
    self.left = None
    self.right = None

class PeopleBSTree:
  def __init__(self):
    self.root = None
  def insert(self, new_person):
    def __insertRecursive(node, new_person):
      if new_person.id < node.person.id:
        if node.left is None:
          node.left = Node(new_person)
          return node.left, 1
        return __insertRecursive(node.left, new_person)
      elif new_person.id > node.person.id:
        if node.right is None:
          node.right = Node(new_person)
          return node.right, 1
        return __insertRecursive(node.right, new_person)
      else:
        # Trả về 2 cho biết id này đã tồn tại, để main không cập nhật thông tin mới
        return node, 2
    if self.root:
      return __insertRecursive(self.root, new_person)
    self.root = Node(new_person)
    # Trả về 1 cho biết id chưa tồn tại, main có thể update info của nhân viên
    return self.root, 1

  def delete(self, person_id):
    # Chức năng tìm node có id nhỏ nhất trong nhánh BS con
    def __findMinNode(node):
      while node.left:
        node = node.left
      return node
    def __deleteRecursive(node, person_id):
      if not node:
        return None
      if person_id<node.person.id:
        node.left = __deleteRecursive(node.left, person_id)
      elif person_id>node.person.id:
        node.right = __deleteRecursive(node.right, person_id)
      else:
        # Khi node hiện tại khớp với person_id thì kiểm tra nhánh trái nhánh phải
        # nếu 1 trong nhánh trống thì trả về nhánh còn lại
        if not node.left:
          return node.right
        elif not node.right:
          return node.left
        # Khi node có đủ 2 nhánh ta đi tìm node nhỏ nhất trong nhánh lớn
        # vì node nhỏ luôn phải nằm nhánh bên trái
        minNode = __findMinNode(node.right)
        # Thay dữ liệu nhân viên bằng dữ liệu node nhỏ nhất
        node.person = minNode.person
        # Hủy dữ liệu của node nhỏ nhất trong nhánh lớn bằng đệ quy
        node.right = __deleteRecursive(node.right, minNode.person.id)
      return node
    return __deleteRecursive(self.root, person_id)
    
  def search(self, person_id):
    def __searchRecursive(node, person_id):
      if not node:
        return None
      if node.person.id == person_id:
        return node
      if person_id<node.person.id:
        return __searchRecursive(node.left, person_id)
      if person_id>node.person.id:
        return __searchRecursive(node.right, person_id)
    return __searchRecursive(self.root, person_id)

  # Phương thức đưa các node trong BST theo thứ tự inorder vào hàng đợi `queue`
  # bằng cách dùng 1 chương trình con đệ quy
  def inOrderQueue(self, queue):
    def __inOrderTraversal(node):
      if node.left:
        __inOrderTraversal(node.left)
      queue.enqueue(node.person)
      if node.right:
        __inOrderTraversal(node.right)
    __inOrderTraversal(self.root)

  # Phương thức đưa các node trong BST theo thứ tự breath-first vào hàng đợi `queue`
  # tương tự phương thức inorder
  def breadthFirstQueue(self, queue):
    def __breadthFirstTraversal(node):
      queue.enqueue(node.person)
      if node.left:
        __breadthFirstTraversal(node.left)
      if node.right:
        __breadthFirstTraversal(node.right)
    __breadthFirstTraversal(self.root)




