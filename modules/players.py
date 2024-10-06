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
    nombre = input('Ingrese el nombre completo del usuario: ')
    while True:
        ut.borrar()
        nickname = input('Ingrese el nickname del usuario: ')
        if nickname in origin:
            print(msg.errorNickname)
            ut.pausar()
        else:
            break
    newPlayer['nombre'] = nombre
    newPlayer['nickname'] = nickname
    origin[nickname] = newPlayer
    print(f"\nUsuario '{nickname}' registrado con éxito.")
    ut.pausar()