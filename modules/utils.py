import sys
import os

def borrar():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")

def validarOpcion(message:str):
    flag = True
    opciones = ('N','S')
    accion = (input(f'{message}').upper())
    if (accion not in opciones):
        print('La opcion que ingreso no esta permitida...')
        return validarOpcion(message)
    elif (accion == "S"):
        flag = True
    elif (accion == "N"):
        flag = False
    return flag
    
def validarSalida(message:str):
    flag = True
    opciones = ('N','S')
    accion = input(f'{message}').upper()
    if (accion not in opciones):
        print('La opcion que ingreso no esta permitida...')
        return validarSalida(message)
    elif (accion == "S"):
        flag = False
    elif (accion == "N"):
        flag = True
    return flag