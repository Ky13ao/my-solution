def print_formatted(number):
    # your code goes here
    w = len('{0:b}'.format(number))
    for n in range(1,number+1):
      print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(n,w=w))
      
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)