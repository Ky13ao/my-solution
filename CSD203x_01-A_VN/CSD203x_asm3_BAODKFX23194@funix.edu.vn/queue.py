class MyQueue:
  def __init__(self):
    self.orders = []

  # Chức năng thêm 1 item vào hàng chờ
  def enqueue(self, item):
    self.orders.append(item)

  # Chức năng hoàn thành item chờ đầu tiên
  def dequeue(self):
    if self.isEmpty():
      return None
    return self.orders.pop(0)

  # Chức năng trả về hàng chờ đang trống
  def isEmpty(self):
    return len(self.orders)==0

  # Chức năng trả dữ liệu nhân viên trong hàng chờ theo bản theo bảng kiểu chuỗi để in
  def __str__(self):
    if self.isEmpty():
      return 'The searched ID is not valid'
    rows = [self.orders[0].fields]
    # Lưu độ rộng từng cột với các độ dài của các fields
    maxWidths = [len(f) for f in self.orders[0].fields]
    while True:
      item = self.dequeue()
      if not item:
        break
      row = dict(item).values()
      rows.append(row)
      # Cập nhật độ rộng các cột với độ dài từng dòng
      maxWidths = [max(w, len(rw)) for w, rw in zip(maxWidths, row)]
    # Phân cột dòng tiêu đề
    strForReturning = [' | '.join(f'{tf:^{tw}}' for tf, tw in zip(rows[0], maxWidths))]
    # Phân cột các dòng khác trong bảng
    for row in rows[1:]:
      strForReturning += [' | '.join(f'{cell:<{w}}' for cell, w in zip(row, maxWidths))]
    return "\n".join(strForReturning)

