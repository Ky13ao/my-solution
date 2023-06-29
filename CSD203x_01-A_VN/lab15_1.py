# python3
import sys


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

  # Iterate over the text to find matches
  for i in range(text_length - pattern_length + 1):
    # Compare the substring of text with the pattern
    if text[i:i+pattern_length] == pattern:
      # If there's a match, add the starting position to the result list
      result.append(i)
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))