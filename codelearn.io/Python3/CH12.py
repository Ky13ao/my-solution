#Cho dãy a gồm n số nguyên không âm a(1), a(2), ..., a(n) và Q câu hỏi.
#Mỗi câu hỏi sẽ cho biết 3 số X L R, yêu cầu hãy đếm số lần xuất hiện số X trong đoạn từ L đến R. Hay nói cách khác đếm số lượng số nguyên i thỏa mãn 2 điều kiện sau:
##   L ≤ i ≤ R
##   a(i) = X.
#Bạn hãy trả về một mảng gồm Q phần tử, phần tử thứ i là đáp án của câu hỏi thứ i.
#Ví dụ:

# n=7, a=[7,6,2,0,0,6,8], Q=3, query=[[2,1,4],[6,1,6],[7,2,4]]
##   thì countNum(n,a,Q,query)=[1,2,0]
#Giải thích: Mỗi phần tử trong query sẽ là bộ 3 số (X, L, R) theo thứ tự.
#Mảng a: 7 6 2 0 0 6 8 
#Câu hỏi thứ 1: X=2, L=1, R=4 thì đáp án là 1, đó là i=3.
#Câu hỏi thứ 2: X=6, L=1, R=6 thì đáp án là 2, đó là các số i= 2,6.
#Câu hỏi thứ 3: X=7, L=2, R=4 thì đáp án là 0.
#Vậy mảng ta cần trả về tương ứng là [1, 2, 0].

#Đầu vào/Đầu ra:

#[Giới hạn thời gian chạy]: 1 giây với C++, 6 giây với Java và C#, 8s với Python, GO và Js.
#[Đầu vào] integer n:
#Kích thước của mảng a
##  1 ≤ n ≤ 105
#[Đầu vào] array of integer: a
# a.size() = n
# 0 ≤ a[i] ≤ 105
#[Đầu vào] integer Q:
#1 ≤ Q ≤ 105
#[Đầu vào] matrix of integer: query
#query.size() = Q
#query[i].size() = 3
#X = query[i][0], L = query[i][1], R = query[i][2]
#1 ≤ L ≤ R ≤ n
#0 ≤ X ≤ 105
#[Đầu ra] array of int
#Một mảng gồm Q phần tử, phần tử thứ i là đáp án của câu hỏi thứ i.

def count_num(n,a,Q,query):
  return [sum(a[i]==q[0] for i in range(q[1],q[2]+1)) for q in query]

n, a, Q, query = 7,[7,6,2,0,0,6,8],3,[[2,1,4],[6,1,6],[7,2,4]]
print(count_num(n,a,Q,query))
