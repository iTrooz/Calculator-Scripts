B=0
L=0
while(1==1):
  try:
    A=input("x=")
    if A=="":
      break
    X=int(A)
    B+=int(input("f("+A+")="))/X
    L+=1
  except ValueError:
    print("Nombre invalide")
   
print(B/L)   