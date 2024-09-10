from sort_lib import *
from search_lib import *
from input_lib import *

def thanks():
	print('Thanks!!!')
	exit()

def mainMenu():
	# Tạo biến dict cho context main menu, gồm tiêu đề và command cần thiết
	arrThru = []
	contextMenu = {"1": {"context":"Manual Input", "command": manualInput},
								 "2": {"context":"File Input", "command": fileInput},
								 "3": {"context":"Bubble sort", "command": lambda: bubbleSort(arrThru, "OUTPUT1.TXT")},
								 "4": {"context":"Selection sort", "command": lambda: selectionSort(arrThru, "OUTPUT2.TXT")},
								 "5": {"context":"Insertion sort", "command": lambda: insertionSort(arrThru, "OUTPUT3.TXT")},
								 "6": {"context":"Search > value", "command": lambda: largerLinearSearch(arrThru, "OUTPUT4.TXT"), "tooltip": "Linear Search"},
								 "7": {"context":"Search = value", "command": lambda: equalsBinarySearch(arrThru, "OUTPUT5.TXT"), "tooltip": "Binary Search"},
								 "0": {"context":"Exit", "command": thanks}
								}

	maxWidth = max([len(key)+len(value['context']) for key, value in contextMenu.items()])+4
	# In context menu ra màn hình
	while True:
		print('+' + '-'*((maxWidth+5)//2-2) + 'Menu' + '-'*((maxWidth+5)//2-2) + '+')
		print('|' + ' '*(maxWidth+5) + '|')
		print('\n'.join(["|   %s. %s%s |" % (i, _["context"], ' '*(maxWidth-len(_["context"])-len(i)-1)) for i, _ in contextMenu.items()]))
		print('+' + '-'*(maxWidth+5) + '+')
		opt = input('[!] Input key menu you wish to run: ').strip()
		if not opt in contextMenu:
			# Kiểm tra lựa chọn có trong menu
			print('[!] Invalid key menu. Try again')
		else:
			# Sau khi kiểm tra tất cả các dữ liệu cần thiết, tiến hành Chạy command đã chọn
			if opt!='0':
				print('[✔] Choice %s: %s' % (opt, contextMenu[opt]['context'] if not 'tooltip' in contextMenu[opt].keys() else contextMenu[opt]['tooltip']))
			arrThru = contextMenu[opt]['command']()

if __name__ == "__main__":
	mainMenu()