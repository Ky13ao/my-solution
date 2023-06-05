# python3

import sys

class Bracket:
  def __init__(self, bracket_type, position):
    self.bracket_type = bracket_type
    self.position = position

  def Match(self, c):
    if self.bracket_type == '[' and c == ']':
      return True
    if self.bracket_type == '{' and c == '}':
      return True
    if self.bracket_type == '(' and c == ')':
      return True
    return False

if __name__ == "__main__":
  # text = sys.stdin.read()
  text = "[]" #tc1
  text = "{}[]" #tc2
  text = "[()]" #tc3
  text = "(())" #tc4
  text = "{[]}()" #tc5
  text = "{" #tc6
  text = "{[}" #tc7 
  text = "foo(bar);" #tc8
  text = "foo(bar[i);" #tc9
  opening_brackets_stack = []
  result = ''
  for i, next in enumerate(text):
    if next == '(' or next == '[' or next == '{':
      # Process opening bracket, write your code here
      opening_brackets_stack.append(Bracket(next, i))

    if next == ')' or next == ']' or next == '}':
      # Process closing bracket, write your code here
      if opening_brackets_stack[-1].Match(next):
        opening_brackets_stack.pop()
      else:
        result = str(i+1)
        break
  if len(opening_brackets_stack)>0 and result=='':
    result = '1'
  # Printing answer, write your code here
  if result =='':
    print('Success')
  else:
    print(result)