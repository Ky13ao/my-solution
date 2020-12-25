# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
S = []
for i in range(0,T):
  S.append(input())
  sOdd = ''
  sEven = ''
  for j in range(len(S[i])):
    if(j % 2 == 0):
      sEven += S[i][j]
    else:
      sOdd += S[i][j]
  print(sEven + ' ' + sOdd)