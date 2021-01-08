def minion_game(string):
  # your code goes here
  str_len = len(string)
  t_sub = str_len*(str_len+1)//2
  kevin = sum(str_len - i for i in range(str_len) if string[i] in 'AEIOU')
  stuart = t_sub - kevin
  print(f'Stuart {stuart}' if stuart>kevin else f'Kevin {kevin}' if stuart<kevin else 'Draw')
    
  
if __name__ == '__main__':
    s = input()
    minion_game(s)