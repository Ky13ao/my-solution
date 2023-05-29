def bubbleSort(a, file_path):
  #Phương pháp bubbleSort
  # duyệt ngược mảng và kiểm tra mảng đã thỏa điều kiện giá trị nhỏ đứng trước
  f = open(file_path, 'w')
  for i in range(len(a)-1, 0, -1):
    swapped = True
    for j in range(i):
      if a[j]>a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        swapped = False
    print(*a)
    print(*a, file=f)
    if swapped:
      break
  f.close()
  return a

def insertionSort(a, file_path):
  #Phương pháp insertionSort
  # là tìm ra giá trị lớn hơn trước vị trí đang duyệt để đưa giá trị đó ra sau
  f = open(file_path, 'w')
  for i in range(1, len(a)):
    idx = i
    value = a[i]
    while idx>0 and a[idx-1]>value:
      a[idx]=a[idx-1];
      idx-=1
    a[idx]=value
    print(*a)
    print(*a, file=f)
  f.close()
  return a

def selectionSort(a, file_path):
  #Phương pháp selectionSort 
  # là tìm ra giá trị bé nhất để đưa về vị trí đầu trong n-1 lượt
  f = open(file_path, 'w')
  for i in range(len(a)-1):
    m = i
    for j in range(i+1, len(a)):
      if a[m] > a[j]:
        m = j
    if i!=m:
      a[i], a[m] = a[m], a[i]
    print(*a)
    print(*a, file=f)
  f.close()
  return a
