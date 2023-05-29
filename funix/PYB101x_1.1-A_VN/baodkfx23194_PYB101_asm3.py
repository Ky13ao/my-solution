from time import time
import json, xml.etree.ElementTree as et, urllib.request as ur



deptListItems={}
empListItems={}

def getTaxPercent(salary_mil):
	# Gán đường link chứa thông tin Thuế TNCN đề bài đã cho
	taxUri = "https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7"
	# Mở kết nối và kiểm tra kết nối thành công
	response = ur.urlopen(taxUri)
	if response.getcode() == 200:
		# Nếu thành công, lưu lại kết quả offline để dùng khi kết nối ko thành công
		content = response.read()
		open('tax.xml', 'wb').write(content)
		taxParams = et.fromstring(content)
	else:
		# Đọc thông tin từ file tax.xml offline
		taxParams = et.parse('tax.xml').getroot()
	#Khởi tạo biến percent = 0
	taxPercentValue=0
	for _ in taxParams:
		# Khởi tạo param tạm trong vòng lặp để làm phép thử các phần tử tax
		param = {}
		for attr in ['min', 'max', 'value']:
			# Tìm các khóa nếu tìm thấy thì ép kiểu float rồi gán vào param tạm
			valueFind = _.find('./'+attr)
			if valueFind != None:
				param[attr] = float(valueFind.text)
		# Nếu phần tử ko có khóa max thì chỉ cần so sánh khóa min và dừng vòng lặp nếu thỏa điều kiện min < lương cơ bản <= max		
		if param['min'] < salary_mil and (not 'max' in param.keys() or param['max'] >= salary_mil):
			taxPercentValue = param['value']
			break
	# Cuối cùng trả về giá trị khóa value 
	return taxPercentValue/100

def getLateComingFine(number_of_times):
	# Gán đường link chứa thông tin mức phạt đi muộn
	lateLimitUri = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de'
	# Mở kết nối và kiểm tra kết nối thành công
	response = ur.urlopen(lateLimitUri)
	if response.getcode() == 200:
		# Nếu thành công, lưu lại kết quả offline để dùng khi kết nối ko thành công
		content = response.read()
		open('late_coming.json', 'wb').write(content)
	else:
		content = open('late_coming.json', 'r').read()
	# Parse chuỗi json thành dict với function loads trong thư viện json
	lateComingParams = json.loads(content)
	# Tìm nhanh giá trị value thỏa điều kiện 
	lateComingFineValue = 0
	for paramIdx, param in enumerate(lateComingParams):
		if param['min'] < number_of_times and (not 'max' in param.keys() or param['max'] >= number_of_times):
			lateComingFineValue = param['value']
			break
	# Trả về kết quả đã tính toán như đề bài
	return lateComingFineValue*number_of_times

class Employee():
	''' Mô tả thuộc tính lớp Employee
	id: Mã số nhân viên
	name: Họ và tên nhân viên
	salary_base: Hệ số lương cơ bản
	working_days: Số ngày làm việc trong tháng
	department: Mã bộ phận
	working_performance: Hệ số hiệu quả
	bonus: Thưởng
	late_comming_days: Số ngày đi muộn
	'''
	position = "Nhân viên"
	def __init__(self, id, name, salary_base, working_days, department, working_performance, 
							 bonus, late_comming_days):
		self.id =  id
		self.name = name
		self.salary_base = salary_base
		self.working_days = working_days
		self.department = department
		self.working_performance = working_performance
		self.bonus = bonus
		self.late_comming_days = late_comming_days

	def totalNoBonusSalary(self):
		# tổng thu nhập chưa thưởng = (salary_base * working_days) * working_performance
		return self.salary_base * self.working_days * self.working_performance

	def totalIncome(self):
		# tổng thu nhập  = tổng thu nhập chưa thưởng + bonus - phạt đi muộn | + thưởng bộ phận | <- dành cho Manager
		return self.totalNoBonusSalary() + self.bonus - self.totalLateComingFine()

	def totalNoTaxSalary(self):
		# tổng thu nhập chưa thuế = tổng thu nhập * 89.5 %
		return self.totalIncome() * 0.895

	def totalLateComingFine(self):
		# tính tiền phạt đi muộn cần phải trừ
		return getLateComingFine(self.late_comming_days)

	def totalTax(self):
		# tính thuế TNCH cần chi trả
		taxPercent = getTaxPercent(self.salary_base/1e6)
		return self.salary_base*taxPercent

	def printPayslip(self):
		# lương thực nhận = tổng thu nhập chưa thuế - khoản thuế cần nộp
		salary = self.totalNoTaxSalary() - self.totalTax()
		# in bảng lương
		print(f'Thu nhập thực nhận: {salary:,.0f} (VND)')
	
	def __iter__(self):
		# Tạo yield để xuất instance dạng dict
		yield 'department', self.department
		yield 'name', self.name
		yield 'salary_base', self.salary_base
		yield 'working_days', self.working_days
		yield 'working_performance', self.working_performance
		yield 'bonus', self.bonus
		yield 'late_comming_days', self.late_comming_days
		yield 'position', 'NV'

	def __str__(self):
		# Tạo str converter để dễ in hơn
		return f'Mã số: {self.id}\nMã bộ phận: {self.department}\nChức vụ: {self.position}\nHọ và tên: {self.name}\nHệ số lương: {self.salary_base:,.0f} (VND)\nSố ngày làm việc: {self.working_days} (ngày)\nHệ số hiệu quả: {self.working_performance}\nThưởng: {self.bonus:,.0f} (VND)\nSố ngày đi muộn: {self.late_comming_days}'

class Manager(Employee):
	'''
	Lớp Manager: Quản Lý kế thừa toàn bộ thuộc tính của lớp Employee
	'''
	position = "Quản Lý"
	def __iter__(self):
		# Tạo yield đè thuộc tính position
		yield from super().__iter__()
		yield 'position', 'QL'

	def totalIncome(self):
		# Ghi đè tổng thu nhập để cộng thêm thưởng bộ phận
		return super().totalIncome() + deptListItems[self.department].bonus_salary


class Department():
	'''
	id: Mã bộ phận
	bonus_salary: Thưởng bộ phận
	'''

	def __init__(self, id, name, bonus_salary):
		self.id = id
		self.name = name
		self.bonus_salary = bonus_salary

	def __str__(self):
		return f"Mã bộ phận: {self.id} \nTên bộ phận: {self.name} \nThưởng bộ phận: {self.bonus_salary:,.0f} (VND)"

	def __iter__(self):
		yield 'name', self.name
		yield 'bonus_salary', self.bonus_salary

def mainMenu():
	# Tạo biến dict cho context main menu, gồm tiêu đề và command cần thiết
	contextMenu = {"1": {"subtitle":"Hiển thị danh sách nhân viên", "command": lambda: listPrint(empListItems)},
								 "2": {"subtitle":"Hiển thị danh sách bộ phận", "command": lambda: listPrint(deptListItems)},
								 "3": {"subtitle":"Thêm nhân viên mới", "command": addNewEmp},
								 "4": {"subtitle":"Xóa nhân viên theo ID", "command": removeEmpById},
								 "5": {"subtitle":"Xóa bộ phân theo ID", "command": removeDeptById},
								 "6": {"subtitle":"Hiển thị bảng lương", "command": printPayslipOfEmpById},
								 "7": {"subtitle":"Thoát", "command": exit},
								 "8": {"subtitle":"Chỉnh sửa nhân viên theo ID", "command": updateEmpById},
								}
	# In context menu ra màn hình
	print('\n'.join(["%s. %s." % (i, _["subtitle"]) for i, _ in contextMenu.items()]))
	opt = input('Mời bạn nhập chức năng mong muốn: ').strip()
	if not opt in contextMenu:
		print('Khóa chức năng bạn đã nhập không phù hợp!')
		exit()
	# Sau khi kiểm tra tất cả các dữ liệu cần thiết, tiến hành nạp trước data Department và Employee
	loadDeptList()
	loadEmpList()
	# Chạy command đã chọn
	contextMenu[opt]['command']()



def attrValid(value_input, condition=lambda _: True, if_fail=None, if_blank=None):
	# Function này dùng để kiểm tra dữ liệu nhập có khớp với điều kiện cho sẵn với tùy chọn cho phép để trống nếu if_blank có giá trị
	if len(value_input):
		if condition(value_input):
			if value_input.isnumeric():
				return float(value_input)
			else:
				return value_input
		else:
			if if_fail.__code__.co_argcount == 0:
				if_fail()
				exit()
			elif if_fail.__code__.co_argcount == 1:
				if_fail(value_input)
				return value_input
	elif if_blank == None:
		print("Bạn không được bỏ trống thông tin này")
		exit()
	else:
		return if_blank

def printPayslipOfEmpById():
	print('---')
	global empListItems
	# Kiểm tra mã số NV đã tồn tại hay chưa và in bảng lương
	empId = attrValid(input('Nhập mã số NV: ').strip(), lambda _: _ in empListItems, lambda: print('Mã nhân viên không tồn tại'))
	empListItems[empId].printPayslip()
	print('---')

def updateEmpById():
	print('---\nChỉnh sửa nhân viên')
	global empListItems
	# Kiểm tra mã số NV đã tồn tại hay chưa và lấy object từ trong global list
	empId = attrValid(input('Nhập mã số NV: ').strip(), lambda _: _ in empListItems, lambda: print('Mã nhân viên không tồn tại'))
	empObj = empListItems[empId]
	empObj.name = attrValid(input('Nhập họ và tên: ').strip(), if_blank=empObj.name)
	# Kiểm tra chức vụ và tiếng hành thay đổi Class nếu có thay đổi
	empClassName = {'Employee':'NV','Manager':'QL'}[type(empObj).__name__]
	empClass = attrValid(input('Nhập chức vụ (NV/ QL): ').strip(), lambda _: _ in ["NV", "QL"], lambda: print("Chức vụ không phù hợp"), if_blank=empClassName)
	if empClassName!=empClass:
		empObj.__class__ = {'NV':Employee, 'QL': Manager}[empClass]
	# Kiểm tra các thông tin nhập vào nếu trống trả về giá trị if=blank
	empObj.salary_base = attrValid(input('Nhập hệ số lương: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'), if_blank=empObj.salary_base)
	empObj.working_days = attrValid(input('Nhập số ngày làm việc: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'), if_blank=empObj.working_days)
	empObj.working_performance = attrValid(input('Nhập hệ số hiệu quả: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'), if_blank=empObj.working_performance)
	empObj.bonus = attrValid(input('Nhập thưởng: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'), if_blank=empObj.bonus)
	empObj.late_comming_days = attrValid(input('Nhập số ngày đi muộn: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'), if_blank=empObj.late_comming_days)
	empData = getData('employee_data.json')
	empData[empId] = dict(empObj)
	saveData('employee_data.json', empData)
	print('Đã hoàn tất chỉnh sửa')
	# In lại nhân viên 1 lần nửa
	print(str(empObj))
	print('---')

def removeEmpById():
	print('---')
	# Đọc data và remove dòng nhân viên đúng với mã số NV đã nhập
	empData = getData('employee_data.json')
	empId = attrValid(input('Nhập mã số NV: ').strip(), lambda _: _ in empData, lambda: print('Mã nhân viên không tồn tại'))
	del empData[empId]
	# Lưu data 
	saveData('employee_data.json', empData)
	print('Đã xóa thành công')
	print('---')

def removeDeptById():
	print('---')
	# Nhận thông tin mã bộ phận:
	deptData = getData('dept_data.json')
	deptId = attrValid(input('Nhập mã bộ phận: ').strip(), lambda _: _ in deptData, lambda: print('Mã bộ phận không tồn tại'))
	# Kiểm tra có nhân viên nào thuộc mã bộ phận ko
	global empListItems
	for _ in empListItems.values():
		if _.department == deptId:
			print("Bạn không thể xóa bộ phận đang có nhân viên")
			exit()
	del deptData[deptId]
	# Lưu data 
	saveData('dept_data.json', deptData)
	print('Đã xóa thành công')
	print('---')

def addNewEmp():
	print('---')
	print('Thêm nhân viên mới ...')
	empId = attrValid(input('Nhập mã số NV: ').strip(), lambda _: not _ in empListItems, lambda: print("Mã nhân viên đã tồn tại"))
	deptId = attrValid(input('Nhập mã bộ phận: ').strip(), lambda _: _ in deptListItems, addNewDept)
	empClass = attrValid(input('Nhập chức vụ (NV/ QL): ').strip(), lambda _: _ in ["NV", "QL"], lambda: print("Chức vụ không phù hợp"))
	empFullName = attrValid(input('Nhập họ và tên: ').strip())
	empSalaryBase = attrValid(input('Nhập hệ số lương: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'))
	empDaysOfWorking = attrValid(input('Nhập số ngày làm việc: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'))
	empPerfomance = attrValid(input('Nhập hệ số hiệu quả: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'))
	empSalaryBonus = attrValid(input('Nhập thưởng: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'))
	empLatesOfComing = attrValid(input('Nhập số ngày đi muộn: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'))
	empClassObj = {"NV": Employee, "QL": Manager}[empClass]
	empObj = empClassObj(empId, empFullName, empSalaryBase, empDaysOfWorking, deptId, empPerfomance, empSalaryBonus, empLatesOfComing)
	global empListItems
	empListItems[empId] = empObj
	print('Đã thêm nhân viên mới ...\n%s' % str(empObj))
	empData = getData('employee_data.json')
	empData[empId] =dict(empObj)
	saveData('employee_data.json', empData)


def addNewDept(dept_id=''):
	if len(dept_id):
		print("Mã bộ phận chưa tồn tại, tạo mới ...")
		deptId = dept_id
	else:
		deptId = attrValid(input('Nhập mã bộ phận: ').strip(), lambda _: not _ in deptListItems, lambda: print("Mã nhân viên đã tồn tại"))
	deptName = attrValid(input('Nhập tên bộ phận: ').strip())
	deptBonus = attrValid(input('Nhập thưởng bộ phận: ').strip(), lambda _: _.replace(".","",1).isnumeric(), lambda: print('Bạn phải nhập một số không âm'))
	dept = Department(deptId, deptName, deptBonus)
	global deptListItems
	deptListItems[deptId] = dept
	print('Đã tạo bộ phận mới ...')
	deptData = getData('dept_data.json')
	deptData[deptId] = dict(dept)
	saveData('dept_data.json', deptData)

def listPrint(list_items):
	print('---')
	print('\n---\n'.join(list(map(str,list_items.values()))))
	print('---')

def loadEmpList():
	global empListItems
	empList = getData('employee_data.json')
	if len(empList.keys()):
		for _id, emp in empList.items():
			empClassObj = Employee if emp['position'] == 'NV' else Manager
			empObj = empClassObj(_id, emp['name'], emp['salary_base'], emp['working_days'], emp['department'], emp['working_performance'], emp['bonus'], emp['late_comming_days'])
			empListItems[_id] = empObj

def loadDeptList():
	global deptListItems
	deptList = getData('dept_data.json')
	if len(deptList.keys()):
		deptListItems = {_id: Department(_id, dept['name'], dept['bonus_salary']) for _id, dept in deptList.items()}

def getData(file_path):
	# Chức năng lấy dữ liệu từ file json và trả về dict
	try:
		deptsData = json.loads(open(file_path, 'r').read())
	except FileNotFoundError:
		deptsData = {}
	return deptsData

def saveData(file_path, data):
	# Thủ tục dùng để lưu data theo đường dẫn file_path
	with open(file_path, 'w') as f:
		f.write(json.dumps(data))
		f.close()

if __name__ == '__main__':
	mainMenu()
