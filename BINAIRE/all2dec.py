C=int(input("Base de depart "))
F=["A","B","C","D","E","F"]

def ch(x):
  try:
    return int(x)
  except:
    return 
B=0
A=input("Chiffre ")
L=len(A)
for i in A:
  L-=1
  B+=int(i)*(C**L)
print(B)