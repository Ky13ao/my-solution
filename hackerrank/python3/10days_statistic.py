#Day 0: Mean, Median, and Mode: https://www.hackerrank.com/challenges/s10-basic-statistics/tutorial
def mean_median_mode_value(arraY):
  mean_value = sum(arraY)/len(arraY)
  arraY.sort(reverse=False)
  median_index = len(arraY)//2
  if len(arraY) % 2 == 0:
    median_value = (arraY[median_index] + arraY[median_index - 1])/2
  else:
    median_value = arraY[median_index]
  counts_arraY = []
  for i in range(len(arraY)):
    counts_arraY.append(sum(a==arraY[i] for a in arraY))
  results_arraY = []  
  for i in range(len(arraY)):
    if counts_arraY[i] == max(counts_arraY):
      results_arraY.append(arraY[i])
  return mean_value, median_value, min(results_arraY)
#INPUT
n, X = int(input()), list(map(int, input().rstrip().split()))
#OUTPUT
print('\n'.join(map(str,mean_median_mode_value(X))))

#Day 0: Weighted Mean https://www.hackerrank.com/challenges/s10-weighted-mean/tutorial
#Sum(X*W)/Sum(W)
def weighted_mean_value(X, W):
  return ('{:.1f}'.format(sum([a*b for a,b in zip(X,W)])/sum(W)))
#INPUT
n, X, W = int(input()), list(map(int, input().rstrip().split())), list(map(int, input().rstrip().split()))
#OUTPUT
print(weighted_mean_value(X,W))


#Day 1: Quartiles https://www.hackerrank.com/challenges/s10-quartiles/tutorial
def quartiles(ls):
  ls.sort()
  half = len(ls)//2
  from statistics import median
  return (median(ls[:half]), median(ls), median(ls[-half:]))
#INPUT
n, X = int(input()), list(map(int, input().rstrip().split()))
#OUTPUT
print('\n'.join(map(str,quartiles(X))))

# Day 1: Interquartile Range: difference between Q1 & Q3
def Interquartile(n, X, F):
  S = []
  for i in range(n):
    S.extend([X[i]]*F[i])
  S = sorted(S)
  from statistics import median
  half_n = len(S) // 2
  Q1 = median(S[:half_n])
  Q3 = median(S[-(half_n):])
  return Q3-Q1
#INPUT
n, X, F = int(input()), list(map(int, input().rstrip().split())), list(map(int, input().rstrip().split()))
#OUTPUT
print("{:.1f}".format(Interquartile(n, X, F)))

# Day 1: Standard Deviation
def stddev(n, numbers):
  mean = sum(numbers) / n
  variance = sum([((x - mean) ** 2) for x in numbers]) / n
  return variance ** 0.5
#INPUT
n, X = int(input()), list(map(int, input().split()))
#OUTPUT
print("{:.1f}".format(stddev(n, X)))

# Day 2: Basic ProbabilitY: https://www.hackerrank.com/challenges/s10-mcq-1/tutorial
#In a single toss of 2 fair (evenlY-weighted) six-sided dice, find the probabilitY that their sum will be at most 9.
from itertools import product
from fractions import Fraction
p = list(product([1,2,3,4,5,6], repeat=2))
n = sum(sum(x) <= 9 for x in p)
print(Fraction(n, len(p)))
#Answer: 5/6

# Day 2: More Dice
#In a single toss of 2 fair (evenlY-weighted) six-sided dice, find the probabilitY that the values rolled bY each die will be different and the two dice have a sum of 6.
n = sum(sum(x) == 6 for x in p if x[1]!=x[0])
print(Fraction(n, len(p)))
#Answer: 1/9

# Day 2: Compound Event ProbabilitY
urn_x = [1,1,1,1,0,0,0]
urn_Y = [1,1,1,1,1,0,0,0,0]
urn_z = [1,1,1,1,0,0,0,0]
p = [x+Y+z==2 for x in urn_x for Y in urn_Y for z in urn_z]
print(Fraction(sum(p)/len(p)).limit_denominator())
#Answer: 17/42


# Day 3: Conditional ProbabilitY
F = [(1,0),(0,1),(1,1)]
n = sum(sum(x) == 2 for x in F)
print(Fraction(n, len(F)))
#Answer: 1/3

# Day 3: Cards of the Same Suit
#You draw 2 cards from a standard 52-card deck without replacing them. What is the probabilitY that both cards are of the same suit?
#= 1 * 12/51 #1 card * 12 that suit left of 51 cards left
#= 12/51
#Answer: 12/51

# Day 3: Drawing Marbles
#A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. If the first marble drawn is red, what is the probabilitY that the second marble is blue?
#If first marble drawn is red, bag now has 2 red marbles and 4 blue marbles
#= 4 / (2+4) # (#of blue marbles)/(total#of marbles left)
#Answer: 2/3


# Day 4: Binomial Distribution I
def fact(n):
    return 1 if n == 0 else n*fact(n-1)
def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))
def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)
boY, girl = map(float, input().split())
p = boY / (boY + girl)
print('{:.3f}'.format(sum([b(i, 6, p) for i in range(3, 7)])))

# Day 4: Binomial Distribution II
reject_percent, n = map(float, '12 10'.split())
p = reject_percent/100
print("%.3f" %sum(b(r, n, p) for r in (0,1,2))) #  no more than 2 rejects
print("%.3f" %sum(b(r, n, p) for r in range(2, int(n+1)))) #  at least 2 rejects


# Day 4: Geometric Distribution I: https://www.hackerrank.com/challenges/s10-geometric-distribution-1/tutorial
def geometric_prob(p, x):
    g = (1-p)**(x-1) * p
    return(g)

numerator, denominator = map(float, input().split())
x = int(input())
p = numerator/denominator
print("%.3f" %geometric_prob(p, x) )
# Day 4: Geometric Distribution II
# probabilitY that defect is found during the first 5 inspections, 
# ie, 1st batch defect, 2nd batch defect,.., 5th batch defect 
print("%.3f" %sum(geometric_prob(p, i) for i in range(1,6)))


# Day 5: Poisson Distribution I: https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial
# mean = mean number of successes that occur in a specified region
# exp = constant = approximatelY 2.71828
# P(X = x) = ((mean ** k) * exp(-mean)) / factorial(k)

from math import factorial, exp

mean, x = float(input()), int(input())
poisson = ((mean ** x) * exp(-mean)) / factorial(x)
print("%.3f" % poisson)


# Day 5: Poisson Distribution II
mean_A, mean_B = map(float, input().split())
cost_A = 160 + 40*(mean_A + mean_A**2)
print("{%.3f}" %cost_A)
cost_B = 128 + 40*(mean_B + mean_B**2)
print("{%.3f}" %cost_B)


# Day 5: Normal Distribution I: https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial
# mean = mean of normal distribution
# stdev = standard deviation of normal distribution
# x = number of successful outcome

# P(X < x) = 0.5 + 0.5*math.erf((x-mean)/(stdev * 2**0.5))
# Note: P(X < x) = P(X <= x) because P(X = x) = 0 for continuous probabilitY distribution function
def normal_prob(mean, stdev, x):
  import math
  return 0.5 + 0.5*math.erf((x-mean)/(stdev * 2**0.5))

mean, stdev = map(float, '20 2'.split())  # map(float, input().split())
limit = 19.5 # float(input())
limit1, limit2 = map(float, '20 22'.split())  # map(float, input().split())

print( '{:.3f}'.format(normal_prob(mean, stdev, limit)) )
# P( a < X < b ) = P(X < b) - P(X < a)
print( '{:.3f}'.format(normal_prob(mean, stdev, limit2) - normal_prob(mean, stdev, limit1)) )

# Day 5: Normal Distribution II
mean, stdev = map(float, input().split())
limit1, limit2 = float(input()), float(input())
# Note: P(X < x) = P(X <= x) because P(X = x) = 0 for continuous probabilitY distribution function
# P(a < X < b) = P(X < b) - P(X < a)
# P(X > c) = 1 - P(X < c)
print( '%.2f' %((1 - normal_prob(mean, stdev, limit1)) *100) )
print( '%.2f' %((1 - normal_prob(mean, stdev, limit2)) *100) )
print( '%.2f' %(normal_prob(mean, stdev, limit2) *100) )
# note: need to output percentage (not probabilitY)


# Day 6: The Central Limit Theorem I: https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/tutorial
weight_limit = float(input())
n = int(input())
[mean, stdev] = [float(input()) for _ in range(2)]
# BY Central Limit Thereom, for large n, 
# S ~ N(mean_S, stdev_S) approximatelY
mean_S = n*mean
stdev_S = (n**0.5)*stdev
# To find P(S < weight_limit)
print( '%.4f' %normal_prob(mean_S, stdev_S, weight_limit) )

# Day 6: The Central Limit Theorem II
ticket_limit = float(input())
n = int(input())
[mean, stdev] = [float(input()) for _ in range(2)]
# BY Central Limit Thereom, for large n, 
# S ~ N(mean_S, stdev_S) approximatelY
# S = total sum of tickets purchased bY 100 students
mean_S = n*mean
stdev_S = (n**0.5)*stdev
# To find P(S < ticket_limit)
print( '%.4f' %normal_prob(mean_S, stdev_S, ticket_limit) )

# Day 6: The Central Limit Theorem III
# Prob( m-z*s < X < m+z*s ) = 0.95
# z = 1.96
n = int(input())
[mean, stdev] = [float(input()) for _ in range(2)]  # 500, 80
[prob, z] = [float(input()) for _ in range(2)]  # 0.95, 1.96
# population mean ~ N(mean, stdev)
# sample mean ~ N(mean, s), where s = sample stdev = stdev/n**0.5
s = stdev/n**0.5
# lower limit
print('%.2f' %(mean - z*s))
# upper limit
print('%.2f' %(mean + z*s))


# Day 7: Pearson Correlation Coefficient I: https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/tutorial
def correlation_coefficient(n, X, Y):
  mean_x = sum(X) / n
  mean_Y = sum(Y) / n
  stdev_x = (sum([(i - mean_x)**2 for i in X]) / n)**0.5
  stdev_Y = (sum([(i - mean_Y)**2 for i in Y]) / n)**0.5
  covariance = sum([(X[i] - mean_x) * (Y[i] -mean_Y) for i in range(n)])
  return covariance / (n * stdev_x * stdev_Y)
#INPUT
n = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))
#OUTPUT
print('{%.3f}' %correlation_coefficient(n, X, Y))

# Day 7: Spearman's Rank Correlation Coefficient: https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/tutorial
def get_rank(X):
  x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
  return [x_rank[x] for x in X]
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
rx = get_rank(X)
rY = get_rank(Y)
d = [(rx[i] -rY[i])**2 for i in range(n)]
r_s = 1 - (6 * sum(d)) / (n * (n*n - 1))
print('%.3f' % r_s)


# Day 8: Least Square Regression Line
# Example 1: using maths formula
# x = [95,85,80,70,60]
# Y = [85,95,70,65,70]
X, Y = [], []
for _ in range(5):
    i = input().split()
    X.append(int(i[0]))
    Y.append(int(i[1]))
n = len(X)
sumX = sum(X)
sumX_sqr = sumX**2
X_sqr_sum = sum([x**2 for x in X])
sumY = sum(Y)
sum_XxY = sum((x*y) for x,y in zip(X,Y))
b = (n*sum_XxY - sumX*sumY) / (n*X_sqr_sum - sumX_sqr)
mean_Y = sumY/n
mean_X = sumX/n
a = mean_Y - b*mean_X
# to make prediction
X_test = 80
Y_test = a + b * X_test
print("%.3f" %Y_test)   # 78.288

# Day 8: Pearson Correlation Coefficient II
#The regression line of Y on x is 3x + 4Y + 8 = 0,  => y = -8/4 - 3x/4 = -(2 + 3x/4) => aY = -2; bY = -3/4
#the regression line of x on Y is 4x + 3Y + 7 = 0.  => x = -7/4 - 3y/4 = -(7/4 + 3y/4) => aX = -7/4; bX = -3/4
# p = pearson coefficient; 
#from https://www.hackerrank.com/challenges/s10-least-square-regression-line/tutorial, we have:
# bY = p.stdX/stdY => p = bY.stdY/stdX 
# bX = p.stdY/stdX => p = bX.stdX/stdY
# => p^2 = bY*bX = -3/4 * -3/4 = 9/16 => p = [3/4, -3/4]
#What is the value of the Pearson correlation coefficient?
#Answer: -3/4


# Day 9: Multiple Linear Regression: https://www.hackerrank.com/challenges/s10-multiple-linear-regression/tutorial
def multiple_linear_regression(X, Y, Q):
  from sklearn import linear_model
  lm = linear_model.LinearRegression()
  lm.fit(X, Y)
  a = lm.intercept_
  b = lm.coef_
  return [a + sum(bi*f for bi,f in zip(b,x)) for x in Q] 
  
if __name__ == '__main__':
  # m is the no. of observed features; n is the no. of features sets
  [m,n] = list(map(int, input().split()))
  # each n subsequent lines contain m+1 space-sep decimals; the 1st m elements are features and last element is value of Y
  X,Y = [],[]
  for _ in range(n):
    stdin = input().rstrip().split()
    X.append(list(map(float,stdin[:m])))
    Y.append(float(stdin[-1]))
  q = int(input().rstrip())
  Q = [list(map(float, input().rstrip().split())) for _ in range(q)]
  #OUTPUT
  print('\n'.join(map(str,multiple_linear_regression(X, Y, Q))))


## end ##