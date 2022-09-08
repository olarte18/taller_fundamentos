# condicional
print("--------------------------------")
print ("--------MAYOR 3 ENTEROS--------")
print ("--------------------------------")
#input

a= int(input("digite un numero"))
b= int(input("digite un numero"))
c= int(input("digite un numero"))
#procesing
if a>b:
    if a>c:
        mayor=a
    else:
        mayor=c
else:
    if b>c:
        mayor=b
    else:
        mayor= c
#output
print ("--------RESULTADOS--------")
print("el numero mayor es: "+ str(mayor))
#fin