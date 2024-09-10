# Uses python3
import sys
'''2-1.py
Mô tả bài toán
Nhiệm vụ. Mục tiêu của bài toán này là tìm ra số lượng đồng xu tối thiểu cần thiết để đổi giá trị input (một số nguyên) thành tiền xu với mệnh giá 1, 5 và 10.
Định dạng input. Input gồm duy nhất một số nguyên 𝑚.
Ràng buộc. 1 ≤ 𝑚 ≤ 10³.
Định dạng output. Xuất ra số lượng đồng xu tối thiểu với mệnh giá 1, 5, 10 khiến m thay đổi.
Giới hạn thời gian. 5s
'''
def get_change(m):
    #write your code here
    k = 0
    for coinType in [10, 5, 1]:
      while m >= coinType:
        m-=coinType
        k+=1
    return k

if __name__ == '__main__':
    # m = int(sys.stdin.read())
    m = int(input())
    print(get_change(m))