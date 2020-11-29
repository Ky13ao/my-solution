from itertools import product
from fractions import Fraction

X, Y, Z = [4,3], [5,4], [4,4]
Xr, Yr, Zr = X[0]/sum(X), Y[0]/sum(Y), Z[0]/sum(Z)
p = (Xr*Yr*(1-Zr))+(Xr*(1-Yr)*Zr)+((1-Xr)*Yr*Zr)

print(Fraction(p).limit_denominator())
# 17/42

