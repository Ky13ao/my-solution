# Viet mot chuong trinh python nhap vao so nguyen N, tinh tong cac so chan tu 0 den N

# N = int(input('Nhap so nguyen: ').strip())
# print(sum([_ for _ in range(N+1) if _ % 2==0]))

# aList = ["a", "b", "c"]
# aTuple = ("a", "b", "c")
# aSet = {"a", "b", "c"}
# aDict = {"a": "valueA", "b": "valueB", "c": "valueC"}

# import urllib.request as ur
# from bs4 import BeautifulSoup

# url = "http://py4e-data.dr-chuck.net/comments_1430669.html"

# res = ur.urlopen(url)

# print(res.read() )
# htmlcontent = BeautifulSoup()

# class Xe():
#   def __init__(self, ten_xe, mau_sac, hang_xe):
#     self.ten_xe = ten_xe
#     self.mau_sac = mau_sac
#     self.hang_xe = hang_xe
#   def hien_thi_thong_tin_xe(self):
#     print("Ten xe: ", self.ten_xe)
  
# class Toyota(Xe):
#   def __init__(self, ten_xe, mau_sac, hang_xe, nguyen_lieu):
#     super().__init__(ten_xe, mau_sac, hang_xe)
#     self.nguyen_lieu = nguyen_lieu
#   def hien_thi_thong_tin_xe(self):
#     print("Ten xe: ", self.ten_xe)

# xe1 = Toyota("Vios", "xanh", "Toyota K", "xe dien")

# xe1.hien_thi_thong_tin_xe()

def tinh_thuong(a, b):
  try:
    print("Thuong ", a/b)
  except ZeroDivisionError:
    print(" Khong duoc chia cho 0")

tinh_thuong(3, 0)