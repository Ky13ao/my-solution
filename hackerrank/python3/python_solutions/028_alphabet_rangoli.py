def print_rangoli(size):
  # your code goes here
  import string
  letters = string.ascii_lowercase[:size]
  [print('-'.join(letters[abs(x):size][::-1] + letters[abs(x-1):size]).center(4*n-3, '-')) for x in range(n, -n, -1) if x !=0]

if __name__ == '__main__':
  n = int(input())
  print_rangoli(n)