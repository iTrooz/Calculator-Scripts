from math import sqrt

A=int(input("N="))
print("Diviseurs :")
B=0
for i in range(1, sqrt(A)):
  if A%i==0:
    print((i,A//i))
    B+=2
print(B,"Diviseurs")