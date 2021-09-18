from math import sqrt

def format(x):
    return str(round(x, 3))

def f(S):
  try:
    S=eval(S)
  except:
    raise ZeroDivisionError
  return S

    

D = {}
e=0

print("Saisie en cours")
while 1==1:
    try:
        x = input("Entrer x : ")
        if x == "":
            break
    
        x = f(x)
        if x in D:
          print(x,"deja present !")
          continue
        
        proba = f(input("Entrer prob : "))
    except ZeroDivisionError:
        print("Saisie invalide !")
        continue
    D[x] = proba
    e+=proba*x

print("Esperance : "+format(e))

v = 0
for x,proba in D.items():
    v+=proba*(x-e)**2

print("Variance : "+format(v))
print("Ecart-type : "+format(sqrt(v)))