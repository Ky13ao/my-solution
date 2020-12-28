# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(number):
  if number==1:
    return 'Not prime'
  if number**0.5 < 2:
    return 'Prime'
  for i in range(2,int(number**0.5)+1):
    if number % i == 0:
      return 'Not prime'
  return 'Prime'

for _ in range(int(input())):
  print(isPrime(int(input())))