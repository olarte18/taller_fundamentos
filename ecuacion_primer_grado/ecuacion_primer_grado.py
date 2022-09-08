# Ejercicio No7 resolver una ecuacion de primer grado
print("----------------------------------")
print("---- Para la ecuacion: ax+b=0-----")
print("----------------------------------")


#input 
a= int(input("digite el valor de a: "))
b= int(input ("digite el valor de b: "))

#procesing

if a!=0:
    x=-b/a
    print("el valor de x es: "+ str(x))
else :
    print("el valor de a no puede ser 0")



