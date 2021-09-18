from math import *

A=eval(input("Entrer A: "))
B=eval(input("Entrer B: "))
C=eval(input("Entrer C: "))
print("")
#print("Formule: "+str(A)+"x^2+"+str(B)+"x+"+str(B))

def f(X):
  if X<0:
    return "+"+str(-X)
  return "-"+str(X)

def f2(X):
  T=round(X,2)
  if T%1==0:
    T=int(T)
  return T
  

A1=-B/2*A
B1=A*A1**2+B*A1+C
A1=f2(A1)
de=B**2-4*A*C

print("Delta:",f2(de))
#print("Alpha: "+str(A1))
#print("Beta: "+str(B1))
#print("Canon: "+str(A)+"(x-"+str(A1)+")^2+"+str(B1))


if de==0:
  print("Racine:",A1)
  print("%s(x%s)^2" % (A,f(A1)))
elif de>0:
  X1=f2((-B-sqrt(de))/(2*A))
  X2=f2((-B+sqrt(de))/(2*A))
  print("Racine 1:",X1)
  print("Racine 2:",X2)
  print("(x%s)(x%s)" % (f(X1),f(X2)))
else:
  print("Aucune racine")
