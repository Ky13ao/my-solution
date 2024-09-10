# python3
import sys


def find_pattern0(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  pattern_length = len(pattern)
  text_length = len(text)

  # Iterate over the text to find matches
  for i in range(text_length - pattern_length + 1):
    # Compare the substring of text with the pattern
    if text[i:i+pattern_length] == pattern:
      # If there's a match, add the starting position to the result list
      result.append(i)
  return result

def find_pattern1(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  pattern_length = len(pattern)
  text_length = len(text)

  # áp dụng thuật toán robin-karp
  pattern_hash = hash(pattern)

  # giá trị của đoạn chuỗi với độ dài bằng pattern đầu tiên trong chuỗi
  window_hash = hash(text[:pattern_length])

  # tìm các window khác trùng hash với pattern
  for i in range(text_length - pattern_length + 1):
    if window_hash==pattern_hash:
      # Compare the substring of text with the pattern
      if text[i:i+pattern_length] == pattern:
        # If there's a match, add the starting position to the result list
        result.append(i)
    if i<text_length-pattern_length:
      window_hash = rehash(window_hash,text[i],text[i+pattern_length])
  return result

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  pattern_length = len(pattern)
  text_length = len(text)

  # tạo dãy cache chứa độ dài tiền tố dài nhất cũng là hậu tố
  lps = compute_lps(pattern)

  # khởi tạo vị trí bắt đầu của pattern và text
  i = 0 # vị trí cho pattern
  j = 0 # vị trí cho text
  while j < text_length:
    if pattern[i]==text[j]:
      i+=1
      j+=1
      if i == pattern_length:
        result.append(j-i)
        i=lps[i-1] # dịch chuyển vị trí dựa theo mảng lps tại vị trí i-1
        # chúng ta kiểm tra hậu tố với phần tiếp theo của text sẽ giúp chương trình tối ưu hơn
    else:
      if i != 0:
        i = lps[i-1]
        # khi vị trí i, j ko match với nhau ta so sánh lùi i và giữ j
      else:
        j += 1
        # khi ko lùi được nữa thì tăng j, và so sánh từ đầu pattern
  return result

# hash function phuc vu cho thuat toan robin-karp
def hash(string):
  # Tính giá trị hash của chuỗi bằng cách tổng các giá trị code của các ký tự trong chuỗi
  return sum(ord(c) for c in string)

# rehash function phuc vu cho thuat toan robin-karp
def rehash(hash_value, old_char, new_char):
  # Thay giá trị code char cũ bằng giá trị code char mới
  return hash_value - ord(old_char) + ord(new_char)

# compute_lps function phuc vu cho thuat toan knuth-morris-pratt
def compute_lps(pattern):
  pattern_length = len(pattern)
  lps = [0] * pattern_length
  # đánh dấu độ dài của khớp tiền tố hậu tố dài nhất
  length = 0 
  i = 1
  while i < pattern_length:
    if pattern[i] == pattern[length]:
      length += 1
      lps[i] = length
      i += 1
    else:
      if length!=0:
        length = lps[length-1]
      else:
        lps[i] = 0
        i += 1
  return lps

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))