from random import randint
#import scores as sc

FLOOR="x"
FRUIT="O"
SNAKE="#"

def fr():
  while 1==1:
    A=randint(0,len(M)-1)
    B=randint(0,len(M[0])-1)
    if M[A][B]==FLOOR:
      M[A][B]=FRUIT
      return
    

M=[[FLOOR]*20 for i in range(5)]
fr()
M[0][0]=SNAKE
L=[[0,0]]
S=0
OOO=" "
FL=1
while FL==1:
  print("Score:",S)
  for i in range(len(M)):
    N=list(M[i])
    print("".join(N))

  OO=input()
  if OO!="":
    OOO=OO
  
  for O in OOO:
    P=list(L[-1])
  
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
    if C==FRUIT:
      fr()
      S+=1
    elif C==SNAKE:
      print("GAME OVER")
      FL=0
      break
    else:
      P2=L.pop(0)
      M[P2[0]][P2[1]]=FLOOR
  
    M[P[0]][P[1]]=SNAKE
    L.append(P)
 
#sc.auto("snake",S)
