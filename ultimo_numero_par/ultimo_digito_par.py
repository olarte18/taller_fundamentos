# Ejercicio No4 Determinar si es ultimo digito es par
print("---------------...---")
print("--ULTIMO NUMERO PAR--")
print("---------------------")


#input
n= int(input("Digite un número entero: "))

# procesing
c= n%10
m= c%2
if m ==0 :
    m= print("es par")
else:
    m= print("no es par")

print ("-----RESULTADOS-----")
