import netrc
from numbers import Rational
import numbers
from this import d
from tkinter import N
import numpy as np
import math
import matplotlib.pyplot as plt
import os
from fractions import Fraction
from sympy import *

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
    math.gcd()
    class fractions.Fraction(float)
        Rational(int n,int d)
        num == n
        den == d
        float("Introduzca el numerador",n)
        float("Introduzca el denominador",d)

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
