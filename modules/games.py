import copy
import random
import modules.utils as ut
import modules.core as cr
import modules.messages as msg
import modules.players as pl

opciones = ['piedra', 'papel', 'tijera']

# Jugador vs IA
def rondaIA(origin):
    ut.borrar()
    print('Inicia la ronda\n')
    eleccionIA = random.choice(opciones) # La IA elige una opción al azar
    eleccionJugador = input('Escribe tu elección piedra, papel o tijera: ').lower() # El jugador elige su jugada
    while eleccionJugador not in opciones:
        eleccionJugador = input('Opción inválida. Escribe nuevamente tu elección piedra, papel o tijera: ').lower()
    ut.borrar()
    print(f'Tu elegiste: {eleccionJugador}')
    print(f'La IA eligió: {eleccionIA}')
    # Determinar el resultado de la ronda
    if eleccionJugador == eleccionIA:
        return 'empate' # Retorno de empate
    elif (eleccionJugador == 'piedra' and eleccionIA == 'tijera') or (eleccionJugador == 'tijera' and eleccionIA == 'papel') or (eleccionJugador == 'papel' and eleccionIA == 'piedra'):
        return 'jugador' # Retorno de usuario como ganador
    else:
        return 'ia' # Retorno de IA como ganador
    
def juegoIA(origin):
    rondasJugador = 0
    rondasIA = 0
    contadorJugador = 0
    contadorIA = 0
    escudoJugador = False
    escudoIA = False
    isJuegoIA = True
    while isJuegoIA:
        ut.borrar()
        nickname = input('Ingrese el nickname del usuario: ')
        if nickname not in origin: # Verificar si el nickname esta disponible
            print(msg.errorNoNickname)
            ut.pausar()
            break
        else:
            ut.borrar()
            print(f'Bienvenido {nickname} inicia el juego vs la IA\n')
            ut.pausar()
            while rondasJugador < 3 and rondasIA < 3: # Criterio mejor de 3 rondas
                resultado = rondaIA(origin)
                if resultado == 'jugador': # Incrementar victorias consecutivas del jugador
                    contadorJugador += 1
                    contadorIA = 0
                    if contadorJugador == 2: # Asignar escudo al jugador
                        escudoJugador = True
                        print('\n¡Has ganado dos rondas consecutivas! Escudo activado')
                    if escudoIA == True: # Verificar escudo de la IA
                        escudoIA = False
                        print('\n¡La IA perdió, pero su escudo la protegió!\n')
                        ut.pausar()
                    else: # Incrementar ronda del jugador
                        rondasJugador += 1
                        print(f'\n¡Ganaste esta ronda! --- Usuario: {rondasJugador} - IA {rondasIA}\n')
                        ut.pausar()
                elif resultado == 'ia': # Incrementar victorias consecutivas de la IA
                    contadorIA += 1
                    contadorJugador = 0
                    if contadorIA == 2: # Asignar escudo a la IA
                        escudoIA = True
                        print('\n¡La IA ha ganado dos rondas consecutivas! Escudo activado')
                    if escudoJugador == True: # Verificar escudo del jugador
                        escudoJugador = False
                        print('\n¡Has perdido, pero tu escudo te protegiós!\n')
                        ut.pausar()
                    else: # Incrementar ronda de la IA
                        rondasIA += 1
                        print(f'\n¡La IA ganó esta ronda! --- Usuario: {rondasJugador} - IA {rondasIA}\n')
                        ut.pausar()
                elif resultado == 'empate': # Validar empate
                    contadorJugador = 0
                    contadorIA = 0
                    print(f'\n¡Empate! --- Usuario: {rondasJugador} - IA {rondasIA}\n')
                    ut.pausar()

            if rondasJugador == 3:
                origin[nickname]['winIA'] += 1  # Asignar victoria del jugador ante la IA
                ut.borrar()
                print(f'¡Felicitaciones ! {nickname} has ganado la partida\n')
                cr.AddData(origin)
                ut.pausar()
                isJuegoIA = False
            else:
                origin[nickname]['loseIA'] += 1  # Asignar derrota del jugador ante la IA
                ut.borrar()
                print('¡Lo siento! La IA ha ganado la partida\n')
                cr.AddData(origin)
                ut.pausar()
                isJuegoIA = False

# Jugador 1 vs 1
def ronda1vs1(origin):
    ut.borrar()
    print('Inicia la ronda\n')
    eleccionJugador1 = input('Jugador 1 escribe tu elección piedra, papel o tijera: ').lower() # El jugador elige su jugada
    while eleccionJugador1 not in opciones:
        eleccionJugador1 = input('Opción inválida. Jugador 1 escribe nuevamente tu elección piedra, papel o tijera: ').lower()
    ut.borrar()
    eleccionJugador2 = input('Jugador 2 escribe tu elección piedra, papel o tijera: ').lower() # El jugador elige su jugada
    while eleccionJugador2 not in opciones:
        eleccionJugador2 = input('Opción inválida. Jugador 2 escribe nuevamente tu elección piedra, papel o tijera: ').lower()
    ut.borrar()
    print(f'Jugador 1 elegió: {eleccionJugador1}')
    print(f'Jugador 2 elegió: {eleccionJugador2}')
    # Determinar el resultado de la ronda
    if eleccionJugador1 == eleccionJugador2:
        return 'empate' # Retorno de empate
    elif (eleccionJugador1 == 'piedra' and eleccionJugador2 == 'tijera') or (eleccionJugador1 == 'tijera' and eleccionJugador2 == 'papel') or (eleccionJugador1 == 'papel' and eleccionJugador2 == 'piedra'):
        return 'jugador1' # Retorno del jugador 1 como ganador
    else:
        return 'jugador2' # Retorno del jugador 2 como ganador
    
def juego1vs1(origin):
    rondasJugador1 = 0
    rondasJugador2 = 0
    contadorJugador1 = 0
    contadorJugador2 = 0
    escudoJugador1 = False
    escudoJugador2 = False
    isJuego1vs1 = True
    while isJuego1vs1:
        ut.borrar()
        nickname = input('Ingrese el nickname del jugador 1: ')
        jugador1 = nickname
        if nickname not in origin: # Verificar si el nickname del jugador 1 esta disponible
            print(msg.errorNoNickname)
            ut.pausar()
            break
        ut.borrar()
        nickname = input('Ingrese el nickname del jugador 2: ')
        jugador2 = nickname
        if nickname not in origin: # Verificar si el nickname del jugador 2 esta disponible
            print(msg.errorNoNickname)
            ut.pausar()
            break
        else:
            ut.borrar()
            print(f'Bienvenidos inicia el juego de {jugador1} vs {jugador2} \n')
            ut.pausar()
            while rondasJugador1 < 3 and rondasJugador2 < 3: # Criterio mejor de 3 rondas
                resultado = ronda1vs1(origin)
                if resultado == 'jugador1': # Incrementar victorias consecutivas del jugador
                    contadorJugador1 += 1
                    contadorJugador2 = 0
                    if contadorJugador1 == 2: # Asignar escudo al jugador 1
                        escudoJugador1 = True
                        print(f'\n¡{jugador1} ha ganado dos rondas consecutivas! Escudo activado')
                    if escudoJugador2 == True: # Verificar escudo del jugador 2
                        escudoJugador2 = False
                        print(f'\n¡{jugador2} perdió, pero su escudo la protegió!\n')
                        ut.pausar()
                    else: # Incrementar ronda del jugador 1
                        rondasJugador1 += 1
                        print(f'\n¡{jugador1} ganó esta ronda! --- {jugador1}: {rondasJugador1} - {jugador2} {rondasJugador2}\n')
                        ut.pausar()
                elif resultado == 'jugador2': # Incrementar victorias consecutivas del jugador 2
                    contadorJugador2 += 1
                    contadorJugador1 = 0
                    if contadorJugador2 == 2: # Asignar escudo al jugador 2
                        escudoJugador2 = True
                        print(f'\n¡{jugador2} ha ganado dos rondas consecutivas! Escudo activado')
                    if escudoJugador1 == True: # Verificar escudo del jugador 1
                        escudoJugador1 = False
                        print(f'\n¡{jugador1} perdió, pero su escudo la protegió!\n')
                        ut.pausar()
                    else: # Incrementar ronda de la IA
                        rondasJugador2 += 1
                        print(f'\n¡{jugador2} ganó esta ronda! --- {jugador1}: {rondasJugador1} - {jugador2} {rondasJugador2}\n')
                        ut.pausar()
                elif resultado == 'empate': # Validar empate
                    contadorJugador1 = 0
                    contadorJugador2 = 0
                    print(f'\n¡Empate! --- {jugador1}: {rondasJugador1} - {jugador2} {rondasJugador2}\n')
                    ut.pausar()

            if rondasJugador1 == 3:
                origin[jugador1]['puntos'] += 2  # Asignar puntos al jugador 1
                origin[jugador1]['win'] += 1  # Asignar victoria del jugador 1
                origin[jugador2]['lose'] += 1  # Asignar derrota del jugador 2
                ut.borrar()
                print(f'¡Felicitaciones {jugador1} ! Has ganado la partida.\n')
                cr.AddData(origin)
                ut.pausar()
                isJuego1vs1 = False
            else:
                origin[jugador2]['puntos'] += 2  # Asignar puntos al jugador 1
                origin[jugador2]['win'] += 1  # Asignar victoria del jugador 1
                origin[jugador1]['lose'] += 1  # Asignar derrota del jugador 2
                ut.borrar()
                print(f'¡Felicitaciones {jugador2} ! Has ganado la partida.\n')
                cr.AddData(origin)
                ut.pausar()
                isJuego1vs1 = False