#Ejercicio No7 Ecuacion de segundo grado


#input
from re import A


a=int(input("ingrese el valor de a: "))
b=int(input("ingrese el valor de b: "))
c=int(input("ingrese el valor de c: "))
#procesing
p1=((b**2)-(4*a*c))
r= p1**0.5
if p1>=0:
    x1=((-b)+r)/(2*a)
    x2=((-b)-r)/(2*a)
    print("el valor de x1 es: "+str(x1))
    print("el valor de x2 es: "+str(x2))
else:
    print("la solucion es imaginaria")



