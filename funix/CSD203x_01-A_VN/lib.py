def quickSort(array, reverse=False):
  # Phương pháp quickSort
  #  chia mảng thành 2 phần và so sánh từng phần với phần tử chốt
  i,j = 0, len(array)-1
  midValue = array[j//2]
  rNum = -1 if reverse else 1
  while i<j:
    while rNum*array[i]<rNum*midValue:
      i+=1
    while rNum*array[j]>rNum*midValue:
      j-=1
    if i<=j:
      array[i], array[j] = array[j], array[i]
      i+=1
      j-=1
  if i < len(array)-1:
    array = array[:i] + quickSort(array[i:], reverse)
  if 0 < j:
    array = quickSort(array[:j+1], reverse) + array[j+1:]
  return array

def count(arr, x):
  if len(arr)==1:
    if arr[0]==x:
      return 1
    else:
      return 0
  else:
    midIdx = len(arr)//2
    print(arr, midIdx, ';  ', end=' ')
    return count(arr[:midIdx], x) + count(arr[midIdx:], x)

def binary_search(a, x):
  left, right = 0, len(a)
  # write your code here
  def search(l, r, x):
    if l>=r:
      if a[l]==x:
        return l
      else:
        return -1
    else:
      m = (l+r)//2
      return max(search(l,m-1,x), search(m,r-1, x)) 
  return search(left, right-1, x)

def bubbleSort(a):
  #Phương pháp bubbleSort
  # duyệt ngược mảng và kiểm tra mảng đã thỏa điều kiện giá trị nhỏ đứng trước
  for i in range(len(a)-1, 0, -1):
    swapped = True
    for j in range(i):
      if a[j]>a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
        swapped = False
        # print('%2d' % j , a)
    if swapped:
      break
  return a

def insertionSort(a):
  #Phương pháp insertionSort
  # là tìm ra giá trị lớn hơn trước vị trí đang duyệt để đưa giá trị đó ra sau
  for i in range(1, len(a)):
    idx = i
    value = a[i]
    while idx>0 and a[idx-1]>value:
      a[idx]=a[idx-1];
      idx-=1
      print(a)
    a[idx]=value
  return a

def selectionSort(a):
  #Phương pháp selectionSort 
  # là tìm ra giá trị bé nhất để đưa về vị trí đầu trong n-1 lượt
  for i in range(len(a)-1):
    m = i
    for j in range(i+1, len(a)):
      if a[m] > a[j]:
        m = j
    if i!=m:
      a[i], a[m] = a[m], a[i]
      print(i, m, a)
    # print(i, a)
  return a



def mergeSort(parent):
  #Phương pháp mergeSort
  # chia mảng làm 2 sort trái sort phải sau đó gộp lại
  #  theo giá trị từ bé đến lớn theo từng phần tử
  def merge(child1, child2):
    newMerge = []
    while len(child1) and len(child2):
      if child1[0]<child2[0]:
        newMerge.append(child1[0])
        del child1[0]
      else:
        newMerge.append(child2[0])
        del child2[0]
    if len(child1):
      newMerge.extend(child1)
    if len(child2):
      newMerge.extend(child2)
    return newMerge
  if len(parent)>1:
    mid = len(parent)//2
    left = mergeSort(parent[:mid])
    right = mergeSort(parent[mid:])
    parent = merge(left, right)
    return parent
  return parent

def shellSort(a):
  #Phương pháp shellSort
  # tương tự insertionSort nhưng so sánh phạm vi rộng hơn
  interval = len(a)
  while interval > 1:
    interval//=2
    for i in range(interval, len(a)):
      j = i
      ai = a[i]
      while j>=interval and a[j-interval]>ai:
        a[j]=a[j-interval]
        j-=interval
      a[j]=ai

  return a

def main():
  # arr = [int(input()) for _ in range(int(input()))]
  # arr = [4, 1, 3, 1,5,2,6,7,9,2,0, 10, 20, 19, 15]
  # arr = [3, 2, 1, 3, 4, 5]
  arr = [13,28,-57,26,-43,4,-22,20,-49,49]
  print(quickSort(arr))
  # print(bubbleSort(arr))
  # print(insertionSort(arr))
  # print(selectionSort(arr))
  # print(mergeSort(arr))
  # print(shellSort(arr))

if __name__ == "__main__":
  main()

