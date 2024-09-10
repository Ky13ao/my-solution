# Uses python3
import sys

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

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input().split()))
    data = [5, 1, 5, 8, 12, 13, 5, 8, 1, 23, 1, 11]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')