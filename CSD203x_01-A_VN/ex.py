def longestChainSymmetry(s):
  oStr = s
  rStr = s[::-1]
  oSLen = len(oStr)
  rSLen = len(rStr)
  oStr = ' ' + oStr
  rStr = ' ' + rStr
  l = [[0] * (rSLen + 1) for _ in range(oSLen + 1)]

  for i in range(1, oSLen + 1):
    for j in range(1, rSLen + 1):
      if oStr[i] == rStr[j]:
        l[i][j] = l[i - 1][j - 1] + 1
      else:
        l[i][j] = max(l[i - 1][j], l[i][j - 1])

  result_str = ""
  while l[oSLen][rSLen] > 0 and oSLen > 0 and rSLen > 0:
    while l[oSLen - 1][rSLen] == l[oSLen][rSLen]:
      oSLen -= 1
    while l[oSLen][rSLen] == l[oSLen][rSLen - 1]:
      rSLen -= 1
    result_str = oStr[oSLen] + result_str
    oSLen -= 1
    rSLen -= 1

  return result_str

s = input()
print(longestChainSymmetry(s))
