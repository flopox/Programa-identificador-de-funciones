from ast import literal_eval
import math
import operator
from os import remove
ops = { "+": operator.add, "-": operator.sub } # etc.

print("Seleccione el tipo de funcion que va a introducir a continuacion.")
print("======================")
print("1->Funcion Racional")
print("2->Funcion Irracional")
print("3->Funcion Algebraica")
print("4->Funcion Exponencial ")
opcion = input("Opcion->")
if opcion == '4':
        base=int(input("ingrese el valor de la base de su funcion"))
        exis=int(input("ingrese el valor de X"))
        print("Su resultado es:")
        print(base**exis)
elif opcion == '1':

        print("division /n ")
        finish = ""
        f= []
        lista=[]
        while finish !='000':
                finish=(input("Terminar pulse 000 \n"))
                f.append(finish)

        equis=int(input("ingrese el valor de x"))
        float(equis)
        h=len(f)
        f.pop()
        

        for k in range(h-1):
                try:
                        op=f[k]
                        lista.append(op)
                        float(op)
                        
                except ValueError:
                        if f[k] == "+":
                                float(f[k-1])
                                float(f[k+1])
                                print(f[k-1]+f[k+1])
                                print(f)
                                print(type(f[k-1]))
                                print(f[k+1])
                                print(type(f[k+1]))
                                print(type(equis))      
                        elif f[k] == "-":
                                float(f[k-1])
                                float(f[k+1])
                                print(f[k-1]-f[k+1])
                                print(lista)
                                print(type(f[k-1]))
                                print(type(f[k+1]))
                        elif f[k] == "*":
                                float(f[k-1])
                                float(f[k+1])
                                print(f[k-1]*f[k+1])
                                print(lista)
                                print(type(f[k-1]))
                                print(type(f[k+1]))
                        elif f[k] == "/":
                                float(f[k-1])
                                float(f[k+1])
                                print(f[k-1]/f[k+1])
                                print(lista)
                                print(type(f[k-1]))
                                print(type(f[k+1]))
                        elif f[k] == "**":
                                float(f[k-1])
                                float(f[k+1])
                                print(f[k-1]**f[k+1])
                                print(lista)
                                print(type(f[k-1]))
                                print(type(f[k+1]))
                        elif f[k] == "//":
                                float(f[k-1])
                                float(f[k+1])
                                print(math.sqrt(f[k+1]))
                                print(lista)
                                print(type(f[k-1]))
                                print(type(f[k+1]))
                        elif f[k] == "x":
                                f[op]=equis