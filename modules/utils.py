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

def validate():
    pass