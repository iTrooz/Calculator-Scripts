P=1
M=""
L=[[] for i in range(7)]

WLEN=4

def sub(x,y,ix,iy):
  C=0
  while 1==1:
    x+=ix
    y+=iy
    if 0<=x<7:
      if 0<=y<len(L[x]):
        if L[x][y]==M:
          C+=1
          continue
    
    return C
      
    
    
    
  

def show():
  for I in range(6):
    I=5-I
    T=""
    for J in range(7):
      K=L[J]
      if I<len(K):
        T+=K[I]
      else:
        T+="#"
          
    print(T)
    
while P!=-1:
  
  show()
  
  R=input("1234567  J "+str(P)+": ")
  try:
    if R[0]==".":
      X=int(R[1])
      Y=int(R[2])
      Z=R[3]

      L[X][Y]=Z
      continue
      
      
    
    
    R=int(R)-1
    if R<0:
      continue
    
    if len(L[R])==6:
      continue
  except:
    continue
  if P==1:
    M="O"
  else:
    M="X"
  C=len(L[R])
  L[R].append(M)
  
  
  V=[0]*4
  V[0]=(0,1)
  V[1]=(1,0)
  V[2]=(1,1)
  V[3]=(1,-1)
  for I in V:
    W=1
    W+=sub(R,C,I[0],I[1])
    W+=sub(R,C,-I[0],-I[1])
    if W>=WLEN:
      show()
      print("Joueur",P,"gagne")
      P=-1
      break
  else:
    P=3-P
    