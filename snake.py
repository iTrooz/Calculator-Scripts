from random import randint
import scores as sc

def fr():
  while 1==1:
    A=randint(0,len(M)-1)
    B=randint(0,len(M[0])-1)
    if M[A][B]=="x":
      M[A][B]="O"
      return
    

M=[["x"]*20 for i in range(5)]
fr()
M[0][0]="#"
L=[[0,0]]
S=0
while 1==1:
  print("Score:",S)
  for i in range(len(M)):
    N=list(M[i])
    print("".join(N))

  P=list(L[-1])
  O=input()
  if O=="8":
    if P[0]>0:
      P[0]-=1
  elif O=="2":
    if P[0]+1<len(M):
      P[0]+=1
  elif O=="6":
    if P[1]+1<len(M[0]):
      P[1]+=1
  elif O=="4":
    if P[1]>0:
      P[1]-=1
  else:
    continue
    
  C=M[P[0]][P[1]]
  if C=="O":
    fr()
    S+=1
  elif C=="#":
    print("GAME OVER")
    break
  else:
    P2=L.pop(0)
    M[P2[0]][P2[1]]="x"
  
  M[P[0]][P[1]]="#"
  L.append(P)
  
sc.auto("snake",S)
