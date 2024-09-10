# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

# Compute the hash value of a string using Rabin-Karp algorithm
def polyHash(s, p, x):
  h = 0 
  for c in reversed(s):
    h = (h * x + ord(c)) % p
  return h

# Precompute the hash values of substrings in the text
def precomputeHashes(text, pattern_len, p, x):
  textLen = len(text)
  hashes = [0] * (textLen - pattern_len + 1)
  lastSubstring = text[textLen - pattern_len:]
  hashes[textLen - pattern_len]= polyHash(lastSubstring, p, x)
  y = pow(x, pattern_len, p)
  for i in range(textLen - pattern_len - 1, -1, -1):
    hashes[i] = (x * hashes[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % p
  return hashes

def getOccurrences(pattern, text):
  p = 10**9 + 7
  x = 263
  patternLen = len(pattern)
  textLen = len(text)
  patternHash = polyHash(pattern, p, x)
  # Precompute the hash values of substrings in the text
  hashes = precomputeHashes(text, patternLen, p, x)
  occurrences = []
  for i in range(textLen - patternLen + 1):
    if patternHash != hashes[i]:
      continue
    if text[i: i+patternLen]==pattern:
      occurrences.append(i)
  return occurrences

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(getOccurrences(*read_input()))