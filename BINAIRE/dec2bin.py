from math import ceil


def sign(x, bf2):
  bf2 = str(bf2)
  M=ceil((len(x)+1)/4)*4
  while(M!=len(x)):
    x=bf2+x
  return x


def length(x):
  M=ceil(len(x)/4)*4
  while(M!=len(x)):
    x="0"+x
  return x


def space(x):
  n = ""
  for i in range (len(x)):
    n=n+x[i]
    if(i%4==3):
      n=n+" "
  return n

A=int(input())
B=""
if A<0:
  A=(A*-1)-1
  BF=1
else:
  BF=0

while(1==1):
  
  B=str((A+BF)%2)+B
  A=A//2
  if A==0:
    break
  
if(BF==0):
  print("Resultat non sign   : "+space(length(B)))

print("Resultat sign   : "+space(sign(B, BF)))