if __name__ == '__main__':
  ls = [[input(),float(input())] for _ in range(int(input()))]
  max2nd = sorted(list(set([score for name,score in ls])))[1]
  print(*[name for name, score in sorted(ls) if score == max2nd], sep='\n')