P=0
L=[" "]*9
run=True

while run:
  print("---")
  for I in range(3):
    T=""
    for J in range(3):
      K=9-(I*3+J)
      T=L[K-1]+T
    print(T+"\\")
  print("---")  
  
  
  R=input("Joueur "+str(P+1)+" ")
  try:
    R=int(R)-1
    if not 0<=R<9:
      raise Error()
  except:
    print("Invalide")
    continue
  if L[R] !=" ":
    print("Deja pris")
    continue  
  
  if P==0:
    L[R]="O"
  else:
    L[R]="X"
    
  for i in L:
    if i==" ":
      P=1-P
      print(" ")
      break
  else:
    print("Fin")
    run=False
     