import copy
import random
import modules.utils as ut
import modules.core as cr
import modules.messages as msg
import modules.players as pl

opciones = ['piedra', 'papel', 'tijera']

# Jugador vs IA
contadorJugador = 0
contadorIA = 0
escudoJugador = False
escudoIA = False


def rondaIA(origin):
    """Realiza una ronda de piedra, papel o tijera"""
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
            while rondasJugador < 3 and rondasIA < 3: # Criterio mejor de 3 rondas
                resultado = rondaIA(origin)
                if resultado == 'usuario':
                    rondasJugador += 1
                    print(f"\n¡Ganaste esta ronda! --- Usuario: {rondasJugador} - IA {rondasIA}\n")
                elif resultado == 'ia':
                    rondasIA += 1
                    print(f"\n¡La IA ganó esta ronda! --- Usuario: {rondasJugador} - IA {rondasIA}\n")
                elif resultado == 'empate':
                    print(f"\n¡Es un empate! --- Usuario: {rondasJugador} - IA {rondasIA}\n")

            if rondasJugador == 3:
                origin[nickname]['winIA'] += 1  # Incrementar victorias del jugador
                print("\n¡Felicitaciones! Has ganado la partida.")
                ut.pausar()
                isJuegoIA = False
            else:
                origin[nickname]['loseIA'] += 1  # Incrementar derrotas del jugador
                print("\nLa IA ha ganado la partida.")
                ut.pausar()
                isJuegoIA = False