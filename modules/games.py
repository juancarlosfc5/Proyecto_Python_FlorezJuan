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
    print("Inicia la ronda\n")
    eleccionIA = random.choice(opciones) # La IA elige una opción al azar
    eleccionJugador = input("Escribe tu elección piedra, papel o tijera: ").lower() # El jugador elige su jugada
    while eleccionJugador not in opciones:
        eleccionJugador = input("Opción inválida. Escribe nuevamente tu elección piedra, papel o tijera: ").lower()
    ut.borrar()
    print(f"Tu elegiste: {eleccionJugador}")
    print(f"La IA eligió: {eleccionIA}")
    # Determinar el resultado de la ronda
    if eleccionJugador == eleccionIA:
        return 'empate' # Retorno de empate
    elif (eleccionJugador == 'piedra' and eleccionIA == 'tijera') or (eleccionJugador == 'tijera' and eleccionIA == 'papel') or (eleccionJugador == 'papel' and eleccionIA == 'piedra'):
        return 'usuario' # Retorno de usuario como ganador
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
                if resultado == 'usuario': # Incrementar victorias consecutivas del jugador
                    contadorJugador += 1
                    contadorIA = 0
                    if contadorJugador == 2: # Asignar escudo al jugador
                        escudoJugador = True
                        print("\n¡Has ganado dos rondas consecutivas! Escudo activado.")
                    if escudoIA == True: # Verificar escudo de la IA
                        escudoIA = False
                        print("\n¡La IA perdió, pero su escudo la protegió!")
                    else: # Incrementar ronda del jugador
                        rondasJugador += 1
                        print(f"\n¡Ganaste esta ronda! --- Usuario: {rondasJugador} - IA {rondasIA}\n")
                        ut.pausar()
                elif resultado == 'ia': # Incrementar victorias consecutivas de la IA
                    contadorIA += 1
                    contadorJugador = 0
                    if contadorIA == 2: # Asignar escudo a la IA
                        escudoIA = True
                        print("\n¡La IA ha ganado dos rondas consecutivas! Escudo activado.")
                    if escudoJugador == True: # Verificar escudo del jugador
                        escudoJugador = False
                        print("\n¡Has perdido, pero tu escudo te protegiós!")
                    else: # Incrementar ronda de la IA
                        rondasIA += 1
                        print(f"\n¡La IA ganó esta ronda! --- Usuario: {rondasJugador} - IA {rondasIA}\n")
                        ut.pausar()
                elif resultado == 'empate': # Validar empate
                    print(f"\n¡Empate! --- Usuario: {rondasJugador} - IA {rondasIA}\n")
                    ut.pausar()

            if rondasJugador == 3:
                origin[nickname]['winIA'] += 1  # Asignar victoria del jugador ante la IA
                ut.borrar()
                print("¡Felicitaciones! Has ganado la partida.\n")
                ut.pausar()
                isJuegoIA = False
            else:
                origin[nickname]['loseIA'] += 1  # Asignar derrota del jugador ante la IA
                ut.borrar()
                print("¡Lo siento! La IA ha ganado la partida.\n")
                ut.pausar()
                isJuegoIA = False