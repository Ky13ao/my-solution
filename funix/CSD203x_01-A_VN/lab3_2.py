# Uses python3
import sys
'''lab3.2 
    Giới thiệu bài toán
Một phần tử của dãy có độ dài n được gọi là “phần tử đa số” nếu nó xuất hiện trong dãy nhiều hơn n/2 lần.
    Mô tả bài toán
- Nhiệm vụ. Mục tiêu của bài toán này là kiểm tra xem một dãy input có chứa “phần tử đa số” hay không.
- Định dạng input. Dòng đầu tiên chứa số nguyên n, dòng tiếp theo chứa dãy n số nguyên không âm a0, a1, . . . , an−1.
- Ràng buộc.
    1 ≤ n ≤ 10^5; 0 ≤ ai ≤ 10^9 với mọi 0 ≤ i < n.
- Định dạng output. Xuất ra 1 nếu dãy chứa “phần tử đa số” và 0 nếu ngược lại.
- Giới hạn thời gian. 5s
- Giới hạn bộ nhớ. 512Mb
'''
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    def majorityIn(l, r):
      if l==r:
        return a[l], 1
      m=(r-l)//2+l
      mjLeft = majorityIn(l, m)
      mjRight = majorityIn(m+1, r)
      if mjLeft[0]==mjRight[0]:
        return mjLeft[0], mjLeft[1]+mjRight[1]
      if mjLeft[1]>mjRight[1]:
        return mjLeft[0], sum(1 for i in range(l,r+1) if a[i]==mjLeft[0])
      else:
        return mjRight[0], sum(1 for i in range(l,r+1) if a[i]==mjRight[0])
    mj = majorityIn(left, right-1)
    if mj[1]>len(a)//2:
      return mj[0]
    else:
      return -1

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # n, a = 5, [2, 3, 9, 2, 2]
    n, a = 5, [8, 8, 7, 7, 7]
    # n, a = 4, [1, 2, 3, 4]
    # n, a = 4, [1, 2, 3, 1]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)