import sys
import os

def borrar(): # Función borrar pantalla identificando el sistema operativo
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar(): # Función pausar pantalla identificando el sistema operativo
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")
    
def validarSalida(message:str): # Función validar opcion de salida
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