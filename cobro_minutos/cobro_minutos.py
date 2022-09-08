# Punto No1 cobro de minutos

print("-----------------------")
print("----COBRO MINUTOS------")
print("-----------------------")

#input
m = int(input("Digite la cantidad de minutos usados: "))
n=300
 
#procesing
if m<=3:
    m=n
else:
    m= (m-3)*(50)+n

#output
print("------------RESULTADOS------------")
print("La cantidad de minutos a cobrar es: $"+str(m))
#fin
