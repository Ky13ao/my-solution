

def equalsBinarySearch(a, file_path):
	x = float(input('Please enter searched input value: '))
	left, right = 0, len(a)
	# Chương trình con thực hiện binary search
	def search(l, r, x):
		if l>=r:
			if a[l]==x:
				return l
			else:
				return -1
		else:
			m = (l+r)//2
			m1 = search(l,m,x)
			m2 = search(m+1,r, x)
			if m1>=0 and m2>=0:
				return min(m1, m2)
			return m1 if m2<0 else m2
	p = search(left, right-1, x)
	if p<0:
		print('Not found!')
		print('Not found!', file=open(file_path, 'w'))
	else:
		print('The right position:', p)
		print('The right position:', p, file=open(file_path, 'w'))
	return a

def largerLinearSearch(a, file_path):
	x = int(input('Please enter searched input value: '))
	# Chỗ này đề yêu cầu tìm số lớn hơn mà ví dụ cho là lớn hơn hoặc bằng
	res = [i for i, xi in enumerate(a) if xi>x]
	if len(res)==0:
		print('No value larger found.')
	else:
		print('Larger position: ', *res)
		print('Larger position: ', *res, file=open(file_path, 'w'))
	return a

if __name__=='__main__':
	# a = equalsBinarySearch([9.0, 3.0, 5.0, 6.0, 1.0, 2.0, 4.0, 5.0, 7.0, 5.0, 7.0, 9.0, 4.0, 5.0], "TEST.TXT")
	a = equalsBinarySearch([9.0, 3.0, 5.0, 6.0, 1.0, 2.0, 4.0], "TEST.TXT")
	print(*a)