import numpy as np
import math
import matplotlib.pyplot as plt
import os

def menu():
    os.system("clear")
    print("Seleccione el tipo de funcion que va a introducir a continuacion.")
    print("======================")
    print("1->Funcion Racional")
    print("2->Funcion Irracional")
    print("3->Funcion Algebraica")
    print("4->Salir")
    opcion = input("Opcion->")

    return opcion

def Funcion_Racional():
    os.system("clear")
    print("Funcion Racional")
    print("=============================")
    
    {"cantidad_opciones":1, "cantidad_disponible":50}

    a = elegir(-5,6,0,1)
    n = elegir(-10,10,0)
    letra_de_funcion = choice(["f", "g", "h"])
    recorridos = [Matematica(letra_conjunto("R")),
        Matematica(letra_conjunto("R")+r"-\{0\}"),
        Matematica(fr"[0, +{INF()}["),
        Matematica(fr"]0, +{INF()}["),
        Matematica(fr"]-{INF()}, 0]"),
        Matematica(fr"]-{INF()}, 0[")
    ]

if 0<a and n<0 and n%2==0:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif 0<a and n<0 and n%2==1 and n!=1:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif 0<a and 0<n and n%2==0:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"
elif 0<a and 0<n and n%2==1:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"

elif a<0 and n<0 and n%2==0:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif a<0 and n<0 and n%2==1 and n!=1:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R')+r'-\{0\}')+", su recorrido es"
elif a<0 and 0<n and n%2==0:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"
elif a<0 and 0<n and n%2==1:
    enunciado = "Sea la función "+Matematica(f"{letra_de_funcion}(x)="+Racional(a)*potencia("x",n)) +f". Si el dominio de {letra_de_funcion} es "+Matematica(letra_conjunto('R'))+", su recorrido es"

if 0<a and n<0 and n%2==0:
    contenido_correcto = Matematica(fr"]0, +{INF()}[")
elif 0<a and n<0 and n%2==1 and n!=1:
    contenido_correcto = Matematica(letra_conjunto("R")+r"-\{0\}")
elif 0<a and 0<n and n%2==0:
    contenido_correcto = Matematica(fr"[0, +{INF()}[")
elif 0<a and 0<n and n%2==1:
    contenido_correcto = Matematica(letra_conjunto("R"))

elif a<0 and n<0 and n%2==0:
    contenido_correcto = Matematica(fr"]-{INF()}, 0[")
elif a<0 and n<0 and n%2==1 and n!=1:
    contenido_correcto = Matematica(letra_conjunto("R")+r"-\{0\}")
elif a<0 and 0<n and n%2==0:
    contenido_correcto = Matematica(fr"]-{INF()}, 0]")
elif a<0 and 0<n and n%2==1:
    contenido_correcto = Matematica(letra_conjunto("R"))

recorridos.remove(contenido_correcto)
contenido_2 = choice(recorridos)
recorridos.remove(contenido_2)
contenido_3 = choice(recorridos)
recorridos.remove(contenido_3)
contenido_4 = choice(recorridos)
recorridos.remove(contenido_4)
contenido_5 = choice(recorridos)
recorridos.remove(contenido_5)
    
    pausa()

def Funcion_Irracional():
    os.system("clear")
    print("Funcion Irracional")
    print("=============================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = multiplicar(a,b)
    print(f'{a:5.2f} * {b:5.2f} = {c:5.2f}')
    
    pausa()
def Funcion_Algebraica():
    os.system("clear")
    print("Funcion Algebraica")
    print("=============================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = multiplicar(a,b)
    print(f'{a:5.2f} * {b:5.2f} = {c:5.2f}')
    
    pausa()

def main():
    opcion = "1"
    while opcion != "*":
        opcion = menu()

        if opcion == "1":
            Funcion_Racional()
        elif opcion == "2":
            Funcion_Irracional()
        elif opcion == "3":
            Funcion_Algebraica()

    os.system("clear")
    print("Fin de la calculadora...")

if __name__=='__main__':
    main()