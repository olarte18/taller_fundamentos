# Ejercicio No5 Determinar si los dos ultimos numeros son iguales

print("----------------------")
print("-ULTIMOS DOS DIGITOS--")
print("----------------------")


#input 
n= int(input("Digite un número: "))
#procesing and output
c=n%100
m= c%10
b= c//10
if b==m :
    print("los ultimos dos digitos son iguales")
else:
    print("Los ultimos dos digitos no son iguales")
#fin