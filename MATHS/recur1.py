def u(n): # appell  e dans le eval string, pour calculer l'element precedent
# ( on fonctionne avec n et n+1 pas n-1 et n )'
  return calc(n-1)
  
def calc(n):
  if n == x:
    return fn # valeur min
  a = eval(tu)
  print("Terme "+str(n)+": "+str(a))
  return a


x = int(input("f_rang: "))
fn = float(input("f_terme: "))
tu = input("u(n+1)= ")
print("R  sultat: "+str(calc(int(input("rang_calc: ")))))