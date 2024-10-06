import copy
import modules.utils as ut
import modules.core as cr
import modules.messages as msg

players = {
    'nombre': '',
    'nickname': '',
    'puntos' : None,
    'win' : None,
    'lose' : None,
    'winIA' : None,
    'loseIA' : None,
}

def addPlayer(origin):
    ut.borrar()
    newPlayer = copy.deepcopy(players)
    nombre = input('Ingrese el nombre del usuario: ')
    nickname = input('Ingrese el nickname del usuario: ')
    newPlayer['nombre'] = nombre
    newPlayer['nickname'] = nickname
    if (nickname == 'pass'): #Jugador con nickname creado
        pass
        print(msg.errorNickname)
    else: #Crear jugador
        origin[nickname] = newPlayer
        print(f"Usuario '{nickname}' registrado con éxito.")
        ut.pausar()