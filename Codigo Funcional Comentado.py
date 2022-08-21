from cmath import sqrt
import math 
from tkinter import Y                           #We import the libraries
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
print("Seleccione el tipo de funcion que va a introducir a continuacion.")
print("======================")
print("1->Funcion Racional")
print("2->Funcion Irracional")
print("3->Funcion Algebraica")                  #We ask the user which kind of function wants to calculte   
print("4->Funcion Exponencial ")
print("5->Funcion con limite ")

opcion = int(input("Opcion->"))
x = 0
def k (x):
        global y
        y= ((3000 * x)/x + 1)                     #Before you run the program you have to enter the function here
        return y
if opcion == 1:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))    #We ask the user if he wants to calculate one point or more
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x")) #we ask the user to enter the domain
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)                #We add the X and the Y to a list on order to plot them
                        listaY.append(k(x= j + 1))
                print("Estas son las X",listaX)
                print("Estas son las Y",listaY)             
                plt.plot([listaX],[listaY],'.r')        #here we graph
                plt.show()
        elif des == 2:                                  #If he wants to graph only one point
                x = int(input("ingrese el valor del punto a calcular: ")) 
                k(x)
                print("x =",x,"e y es igual a",y)  #We show the results
                plt.plot(x,y,'.r')                       #We graph
                plt.show()                             
elif opcion == 2:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x"))
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)
                        listaY.append(k(x= j + 1))
                print("Estas son las X",listaX)
                print("Estas son las Y",listaY)        
                plt.plot([listaX],[listaY],'.r')
                plt.show()
        elif des == 2:
                x = int(input("ingrese el valor del punto a calcular: "))
                k(x)
                print("x =",x,"e y es igual a",y)
                plt.plot(x,y,'.r')
                plt.show()
elif opcion == 3:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x"))
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)
                        listaY.append(k(x= j + 1))
                print("Estas son las X",listaX)
                print("Estas son las Y",listaY) 
                plt.plot([listaX],[listaY],'.r')
                plt.show()
        elif des == 2:
                x = int(input("ingrese el valor del punto a calcular: "))
                k(x)
                print("x =",x,"e y es igual a",y)
                plt.plot(x,y,'.r')
                plt.show()
elif opcion == 4:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x"))
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)
                        listaY.append(k(x= j + 1))
                print("Estas son las X",listaX)
                print("Estas son las Y",listaY) 
                plt.plot([listaX],[listaY],'.r')
                plt.show()
        elif des == 2:
                x = int(input("ingrese el valor del punto a calcular: "))
                k(x)
                print("x =",x,"e y es igual a",y)
                plt.plot(x,y,'.r')
                plt.show()
        if des == 1:
                x = 0
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x")) 
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)                
                        listaY.append(k(x= j + 1))
                print("Estas son las X",listaX)
                print("Estas son las Y",listaY)             
                plt.plot([listaX],[listaY],'.r')        
                plt.show()
        elif des == 2:                                 
                x = int(input("ingrese el valor del punto a calcular: ")) 
                k(x)
                print("x =",x,"e y es igual a",y)  
                plt.plot(x,y,'.r')                      
                plt.show() 
if opcion == 5:
        print("1 - muchos \n 2 - uno")
        des=int(input("¿Desea calcular un punto o muchos?"))    
        if des == 1:
                tend= int(input("Ingrese a que numero tiende la funcion")) #We ask the user to enter the number which the function tends       
                x = 0 
                listaX=[]
                listaY=[]
                rang1= int(input("ingrese desde donde se empieza a analizar x")) 
                rang2= int(input("ingrese hasta donde se va a analizar x"))

                for j in range (rang1,rang2):
                        x = j + 1
                        listaX.append(x)                
                        listaY.append(k(x= j + 1))
                print("Estas son las X",listaX)
                print("Estas son las Y",listaY)
                float(tend)
                liz=0.0
                lde=0.0                                #Here we define the variables that we are going to use
                liz= tend-0.1
                print("Este es el limite de izquierda")
                print(k(liz))                        #Here we calculate the left limit        
                print("Este es el limite de derecha")
                lde=tend+ 0.1                        #Here we calculate the right limit
                print(k(lde))
                plt.plot([listaX],[listaY],'.r')      
                plt.show()
        elif des == 2:                                 
                x = int(input("ingrese el valor del punto a calcular: ")) 
                k(x)
                print("x =",x,"e y es igual a",y)  
                plt.plot(x,y,'.r')                     
                plt.show()                                                       


#Link to the repository repositorie https://github.com/flopox/Programa-identificador-de-funciones