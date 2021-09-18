def P(X):
  print(X)

class Sign:
  def calc(self,x,y):
    print(x,y)
    nx=x
    for j in range(y-1):
      nx=L[self.T].calc(nx,x)
    return nx

S=Sign()
S.calc=lambda x,y:x+y
L=[S]
    
for i in range(1,10):
  S2=Sign()
  S2.T=i-1
  L.append(S2)


  #R=L[i].calc(3,2)
  #P(R)