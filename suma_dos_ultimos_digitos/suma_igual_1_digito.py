# Ejercicio No6 suma de los so ultimos digitos y verifficar si es un solo digito

print("------------------------")
print("--SUMA ULTIMOS NUMEROS--")
print("------------------------")


#input 


from math import trunc


n1= int(input("digite un numero: "))
n= abs(n1)
#procesing
c=n%100
m=c%10
b=c//10
b1= (b)
m1= (m)
d=(m1+b1)
if d<=9:
    if d>-10:
        print("la suma de los dos ultimos es: "+str(d)+" lo cual es un numero de un digito")
    else: 
        print("la suma de los dos ultimos es: "+str(d)+" lo cual no es un numero de un digito")
else:
    print("la suma de los dos ultimos es: "+ str(d)+" lo cual no es un numero de un digito")


#fin
    
        