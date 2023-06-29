def khoangcach(x1, y1, x2, y2):
  return ((x1-x2)**2+(y1-y2)**2)**(1/2)

def kiemtra_tamgiac(x1, y1, x2, y2, x3, y3):
  # bat dang thuc tam giac: https://blog.marathon.edu.vn/bat-dang-thuc-tam-giac/
  d1, d2, d3 = khoangcach(x1, y1, x2, y2), khoangcach(x1, y1, x3, y3), khoangcach(x2, y2, x3, y3)
  return d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1

def goc(x0, y0, x1, y1, x2, y2):
  from math import acos, degrees, sqrt
  x01, y01 = x1 - x0, y1 - y0
  x02, y02 = x2 - x0, y2 - y0
  # cong thuc tinh goc giua 2 vecto: https://www.mathvn.com/2019/12/cong-thuc-tinh-goc-giua-hai-vecto-trong.html
  n1An2 = (x01*x02+y01*y02)/(sqrt(x01**2+y01**2)*sqrt(x02**2+y02**2))
  return degrees(acos(n1An2))

def loai_tamgiac(xA, yA, xB, yB, xC, yC):
  gocA = goc(xA, yA, xB, yB, xC, yC)
  gocB = goc(xB, yB, xA, yA, xC, yC)
  gocC = goc(xC, yC, xA, yA, xB, yB)

  if gocA == gocB and gocB == gocC:
    return "Tam giac deu"
  resAngle = "tai dinh "
  if gocA>=90 or gocB==gocC:
    resAngle += "A"
  elif gocB>=90 or gocA==gocC:
    resAngle += "B"
  elif gocC>=90 or gocA==gocB:
    resAngle +="C"
  else:
    return "Tam giac thuong"  

  res = "Tam giac "
  if gocA>90 or gocB>90 or gocC>90:
    res += "tu "
  elif gocA==90 or gocB==90 or gocC==90:
    res += "vuong "
  if gocA==gocB or gocA==gocC or gocB==gocC:
    res += "can "
  return res + resAngle

def dientich_tamgiac(xA, yA, xB, yB, xC, yC):
  d1, d2, d3 = khoangcach(xA, yA, xB, yB), khoangcach(xA, yA, xC, yC), khoangcach(xB, yB, xC, yC)
  # Ap dung cong thuc Heron: https://thuthuatphanmem.vn/cach-tinh-dien-tich-tam-giac-chuan/
  p = (d1+d2+d3)/2
  return (p*(p-d1)*(p-d2)*(p-d3))**(1/2)

def duongcao_tamgiac(xA, yA, xB, yB, xC, yC):
  ab, ac, bc = khoangcach(xA, yA, xB, yB), khoangcach(xA, yA, xC, yC), khoangcach(xB, yB, xC, yC)
  # Ap dung cong thuc Heron: https://thuthuatphanmem.vn/cach-tinh-dien-tich-tam-giac-chuan/
  p = (ab+ac+bc)/2
  s = (p*(p-ab)*(p-ac)*(p-bc))**(1/2)
  # Tra ve gia tri tap hop cac duong cao theo huong dan: https://quantrimang.com/cong-nghe/cong-thuc-tinh-duong-cao-trong-tam-giac-180795
  return {"A": s*2/bc, "B": s*2/ac, "C": s*2/ab}

def trungtuyen_tamgiac(xA, yA, xB, yB, xC, yC):
  def m(a,b,c):
    #Cong thuc: https://kyniemsharp10nam.vn/tu-van-dich-vu/duong-trung-tuyen/
    return ((2*b*b+2*c*c-a*a)/4)**(1/2)
  ab, ac, bc = khoangcach(xA, yA, xB, yB), khoangcach(xA, yA, xC, yC), khoangcach(xB, yB, xC, yC)
  return  {"A": m(bc, ac, ab), "B": m(ac, bc, ab), "C": m(ab, ac, bc)}

def trongtam_tamgiac(xA, yA, xB, yB, xC, yC):
  #Cong thuc tim toa do trong tam tam giac: https://hoctoan24h.net/tim-toa-do-trong-tam-tam-giac-trong-mat-phang-oxy/
  return ((xA+xB+xC)/3, (yA+yB+yC)/3)

def tructam_tamgiac(xA, yA, xB, yB, xC, yC):
  try:
    x = ((xC-xB)*(yA-yC)*xA-(yC-yB)*((yB-yA)*(yA-yC)-(xC-xA)*xB))/((xC-xB)*(yA-yC)+(yC-yB)*(xC-xA))
    y = (xC-xA)*(x-xB)/(yA-yC) + yB
  except ZeroDivisionError:
    x = ((xB-xA)*(yC-yB)*xC-(yB-yA)*((yA-yC)*(yC-yB)-(xB-xC)*xA))/((xB-xA)*(yC-yB)+(yB-yA)*(xB-xC))
    y = (xB-xC)*(x-xA)/(yC-yB) + yA
  return ( x,  y)

def main():
  print('PYB101x - Assignment 01')
  xA, yA, xB, yB, xC, yC = list(map(int, input("Nhập tọa độ [Ax, Ay, Bx, By, Cx, Cy]: ").split(",")))
  # xA, yA, xB, yB, xC, yC = [1, 1, 2, 2, 3, 1]
  # xA, yA, xB, yB, xC, yC = [3, 5, -5, 1, 0, -4]
  print("Do dai AB = %.2f cm." % khoangcach(xA, yA, xB, yB))
  print("Do dai AC = %.2f cm." % khoangcach(xA, yA, xC, yC))
  print("Do dai BC = %.2f cm." % khoangcach(xB, yB, xC, yC))
  if kiemtra_tamgiac(xA, yA, xB, yB, xC, yC):
    print("ABC la mot tam giac")
  else:
    print("ABC khong phai la mot tam giac")
    exit()
  print('Goc BAC = %.2f (do)' % goc(xA, yA, xB, yB, xC, yC))
  print('Goc ACB = %.2f (do)' % goc(xC, yC, xA, yA, xB, yB))
  print('Goc ABC = %.2f (do)' % goc(xB, yB, xA, yA, xC, yC))
  print("Loai cua tam giac ABC:", loai_tamgiac(xA, yA, xB, yB, xC, yC))
  print("Dien tich tam giac ABC = %.2f (cm2)" % dientich_tamgiac(xA, yA, xB, yB, xC, yC))
  cacduongcao = duongcao_tamgiac(xA, yA, xB, yB, xC, yC)
  for dinhduongcao in cacduongcao:
    print(f"Do dai duong cao tu diem {dinhduongcao} = {cacduongcao[dinhduongcao]:.2f} cm")
  cactt = trungtuyen_tamgiac(xA, yA, xB, yB, xC, yC)
  for dinhtt in cactt:
    print(f"Do dai trung tuyen tu diem {dinhtt} = {cactt[dinhtt]:.2f} cm")
  print("Tọa độ trọng tâm của tam giác ABC: x = %.2f; y = %.2f" % trongtam_tamgiac(xA, yA, xB, yB, xC, yC))
  print("Tọa độ trực tâm của tam giác ABC: x = %.2f; y = %.2f" % tructam_tamgiac(xA, yA, xB, yB, xC, yC))

if __name__ == "__main__":
  main()