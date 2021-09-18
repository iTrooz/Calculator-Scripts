L=["A","B","C","D","E","F"]

while 1==1:
  A=int(input("Nombre "))
  B=int(input("Base d'arrivee "))
  R=""

  while(1==1):
    C=A%B
    A=A//B
    if C>9:
      C=L[C-10]
    else:
      C=str(C)
    R=C+R
    if A==0:
      break
  print(R)