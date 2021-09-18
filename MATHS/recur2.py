first = int(input("f_rang: "))
u = float(input("f_terme: "))
# ( u = terme precedant, n = rang precedant )
tu = input("recur= ")
max = int(input("rang_calc: "))

for n in range(first+1, max+1):
		u = eval(tu)
		print("Terme "+str(n)+": "+str(u))
print("Résultat: "+str(u))