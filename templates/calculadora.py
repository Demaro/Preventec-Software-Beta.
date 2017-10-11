import math
def bienvenidos():
    print("Selecciona una opción:")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Divicion")
    print("5 - Potencia")
    print("6 - Raiz")
    print("7 - Porcentaje")
    print("8 - factorial")
    print("9 - coseno")
    print("10- Aproximar")
    print("11- Comparar")

def suma():
    print("Has elegido añadir suma")
    Numero1 = int(input("Numero1: "))
    Numero2 = int(input("Numero2: "))
    print(Numero1+Numero2)
def resta():
    print("Has elegido añadir resta")
    Numero1 = int(input("Numero1: "))
    Numero2 = int(input("Numero2: "))
    print(Numero1-Numero2)
def multiplicacion():
    print("Has elegido añadir multiplicacion")
    Numero1 = str(input("Numero1: "))
    Numero2 = str(input("Numero2: "))
    print(Numero1*Numero2)
def divicion():
    print("Has elegido añadir divicion")
    Numero1 = float(input("Numero1: "))
    Numero2 = float(input("Numero2: "))
    print(Numero1/Numero2)
def potencia():
    print("Has elegido añadir potencia")
    Numero1 = float(input("Numero1: "))
    Numero2 = float(input("Numero2: "))
    print(math.pow(Numero1,Numero2))
def raiz():
    print("Has elegido añadir raiz")
    Numero1 = float(input("Numero1: "))
    Numero2 = float(input("Numero2: "))
    print(math.sqrt(Numero1,Numero2))
def porcentaje():
    print("Has elegido añadir porcentaje")
    Numero1 = float(input("%: "))
    Numero2 = float(input("Numero2: "))
    print(Numero1*Numero2/100)
def factorial():
    print("Has elegido añadir factorial")
    Numero1 = float(input("Numero1: "))
    print(math.factorial(Numero1))
def coseno():
    print("Has elegido añadir coseno")
    Numero1 = float(input("Numero1: "))
    print(math.cos(Numero1))
def aproximar():
    print("Has elegido añadir aproximar")
    Numero1 = float(input("Numero1: "))
    print(math.floor(Numero1))
def comparar():
    print("Has elegido añadir comaracion")
    Numero1 = str(input("Numero1: "))
    Numero2 = str(input("Numero2: "))
    if(Numero1>Numero2):
        print(Numero1 + " es mayor a " +Numero2)
    else:
        print(Numero1 + " es menor a " +Numero2)

def mierror():
    print("La opción que has seleccionado no es válida")
