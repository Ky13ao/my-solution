def manualInput():
	n = input('Please enter input number of elements: ')
	na = input('Please enter input elements: ').strip()
	a = list(map(float, na.split(' ')))
	if len(a) == int(n):
		print(na, file=open('input.txt', 'w'))
		return a
	else:
		print('Invalid input. Try again.')

def fileInput():
  try:
    f = open(input('Please enter the file path: '), 'r')
    a = list(map(float, f.read().split(' ')))
    print(*a)
    return a
  except FileNotFoundError:
    print('File not found. Try again.')
    fileInput()
