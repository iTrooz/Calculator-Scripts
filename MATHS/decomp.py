from math import sqrt
N=int(input("N="))

P=2
SQ=N

def f(x):
  for I in range(x+1,SQ):
    for J in range(1,sqrt(I)):
      if I%J==0:
        break
    else:
      continue
    return I
print("Decomposition:")
while N!=1:
  if N%P==0:
    N=N//P
    print(P)
  else:
    P=f(P)
    
