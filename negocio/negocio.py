#ejercicio No9 

#input 
n=input("Digite el tipo de cliente: General(G) o Afiliado(A):")
p=input("digite el tipo de pago: Contado(c) o Plazos(P): ")
v= int(input("digite el valor de la compra: "))

#procesing
if n=="g" and p=="c":
    t=v-((v*15)/100)
    print("el valor a pagar es: "+ str(t))
if n=="g" and p=="p ":
    t=v-((v*10)/100)
    print("el valor a pagar es: "+str(t))
if n=="a" and p=="c":
    t= v-((v*20)/100)
    print("el valor a pagar es: "+ str(t))
if n=="a" and p=="p":
    t= v-((v*5)/100)
    print("el valor a pagar es: "+str(t))
#fin
