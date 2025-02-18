import copy
import modules.utils as ut
import modules.core as cr
import modules.messages as msg

# Diccionario jugador vacío
players = {
    'nombre': '',
    'nickname': '',
    'puntos' : 0,
    'win' : 0,
    'lose' : 0,
    'winIA' : 0,
    'loseIA' : 0,
}

def addPlayer(origin): # Funcion agregar usuario
    ut.borrar()
    newPlayer = copy.deepcopy(players) # Copiar diccionario players vacio
    nombre = input('Ingrese el nombre completo del usuario: ')
    while True:
        ut.borrar()
        nickname = input('Ingrese el nickname del usuario: ')
        if nickname in origin: # Verificar si el nickname esta disponible
            print(msg.errorNickname)
            ut.pausar()
        else:
            break
    newPlayer['nombre'] = nombre # Insertar el nombre dentro de la copia del diccionario players
    newPlayer['nickname'] = nickname # Insertar el nickname dentro de la copia del diccionario players
    origin[nickname] = newPlayer # Insertar toda la copia del diccionario players dentro del diccionario Origin
    print(f'\nUsuario "{nickname}" registrado con éxito.\n')
    cr.AddData(origin)
    ut.pausar()