import re

def checkStrongPassword0(password):
  if len(password)<6:
    return False
  if all([ord(x) not in range(65,91) for x in password]):
    return False
  if all([ord(x) not in range(97,123) for x in password]):
    return False
  if all([ord(x) not in range(48,58) for x in password]):
    return False
  if all([x not in "!@#$%^&*()-+" for x in password]):
    return False
  return True

def checkStrongPassword(password):
  if len(password)<6:
    return False
  return bool(re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*\(\)-\+\$]).*$", password))


def amendTheSentence(s):
  return re.sub(r"([A-Z])",r" \1", s).lower().strip()

#Một xâu được gọi là palindrome nếu viết xuôi hay viết ngược xâu đó đều cho ra kết quả giống nhau
def checkPalindrome(inputString):
  return inputString==inputString[::-1]

#Xóa các khoảng trắng thừa (kí tự cách) trong xâu kí tự cho trước, 
# sao cho giữa các từ chỉ cách nhau bởi 1 khoảng trống. Cũng không
#  có khoảng trống ở đầu và cuối của xâu
def formatString(input):
    return re.sub(r"( +)",r" ",input).strip()

def isTandemRepeat(inputString):
    if len(inputString)%2!=0:
        return False
    m = len(inputString)//2
    return inputString[:m] == inputString[m:]

print(checkStrongPassword("abc1"))
print(checkStrongPassword("Aa123A!"))
print(checkStrongPassword("AAAAAAAAAAAAAA"))
print(checkStrongPassword("ABC1&!aaaa"))
print(checkStrongPassword("AAAAaaa"))