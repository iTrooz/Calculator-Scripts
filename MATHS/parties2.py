L=[]

while 1==1:
  I=input()
  if I=="":
    break
  L.append(I)

print("------")    
  
for I in range(2**len(L)):
  B=bin(I)[2::]
  M=""
  for J in range(len(B)):
    if B[J]=="1":
      M+=L[J]+" "
  print(M)
