import modules.utils as ut
import modules.core as cr
import modules.messages as msg

players = {
    'nombre': '',
    'nickname': '',
    'puntos' : None,
    'ganados' : None,
    'perdidos' : None,
    'ganadosIA' : None,
    'perdidosIA' : None,
}

def addPlayer(origin):
    ut.borrar()
    nombre = input('Ingrese el nombre del jugador: ')
    nickname = input('Ingrese el nickname del jugador: ')
    if (nickname): #Jugador con nickname creado
        pass
        print('msg.errorNickname')
    else: #Crear jugador
        players['nombre'] = nombre
        players['nickname'] = nickname