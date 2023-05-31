def lab61_01():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/1059946
  print("Ready")

def lab61_02():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/692192
  s = 0
  for _ in range(int(input())):
      s += int(input())
  print(s)

def lab61_03():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/692784
  stdo = []
  for _ in range(int(input())):
      stdo.append(int(input())**2)
  print(*stdo,sep=' ')

def lab61_04():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/692428
  a = []
  for _ in range(int(input())+2):
    a.append(int(input()))
  a.insert(a[-2],a[-1])
  print(*a[:-2],sep=' ') 

def lab61_05():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/692257
  a = [int(input()) for _ in range(int(input())+1)]
  a.pop(a[-1])
  a = a[:-1]
  print(*a)

def lab61_06():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/778960
  def isFactor(n):
    if n<=1:
      return False
    for f in range(2,int(n**0.5)+1):
      if n%f==0:
        return False
    return True

  a = []
  for _ in range(int(input())):
    n = int(input())
    if isFactor(n):
      a.append(n)
  print(*a)

def lab61_07():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/988805
  t = {}
  for _ in range(int(input())):
    n = int(input())
    if n in t:
      t[n] += 1
    else:
      t[n] = 1
  for a in sorted(t.keys()):
    print('{} - {};'.format(a,t[a]),end=' ')
  
def lab61_08():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/990055
  def daydondieu(arr):
    if len(arr)<2:
        return 'YES'
    if a[0]>a[1]:
        c = 1
    elif a[0]<a[1]:
        c = 2
    else:
        return 'NO'
    for _ in range(2,len(arr)):
        if c == 1:
            if a[_-1]<=a[_]:
                return 'NO'
        if c == 2:
            if a[_-1]>=a[_]:
                return 'NO'
    return 'YES'
  a = [int(input()) for _ in range(int(input()))]
  print(daydondieu(a))

def lab61_09():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/989559
  a = [int(input()) for _ in range(int(input()))]
  pos = 0
  for _ in range(int(input())):
      b = int(input())
      for ai in range(pos,len(a)):
          if a[ai] > b:
              a.insert(ai,b)
              break
      if ai == len(a)-1:
          a.append(b)
      pos=ai
  print(*a)

def lab61_10():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/779114
  res = 0
  for _ in range(int(input())*int(input())):
    res += int(input())
  print(res)

def lab61_11():
  # https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/779241
  # So phan tu trong mang la huu han
  # Ton tai 2 phan tu cung gia tri trong cung mot mang
  pass