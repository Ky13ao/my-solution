def merge_the_tools(string, k):
    # your code goes here
    while k<=len(string):
      T = ''
      for i in range(k):
        if string[i] not in T:
          T = T + string[i]
      print(T)
      string = string[k:]
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)