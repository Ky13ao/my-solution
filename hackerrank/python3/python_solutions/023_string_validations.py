if __name__ == '__main__':
  s = input()
  print(sum(_.isalnum() for _ in s)>0)
  print(sum(_.isalpha() for _ in s)>0)
  print(sum(_.isdigit() for _ in s)>0)
  print(sum(_.islower() for _ in s)>0)
  print(sum(_.isupper() for _ in s)>0)