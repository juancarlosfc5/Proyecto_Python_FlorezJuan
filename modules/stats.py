import modules.utils as ut

def viewStats1vs1(origin):
    if not origin: # Verificar si hay jugadores registrados
        print('No existen jugadores registrados')
        return
    # Ordenar jugadores por puntos en orden descendente (de mayor a menor)
    jugadoresOrdenados = sorted(origin.items(), key=lambda jugador: jugador[1]['puntos'], reverse=True)
    # Mostrar los 3 mejores puntajes
    print('\n----- Mejores 3 Puntajes -----')
    for i, (nickname, datos) in enumerate(jugadoresOrdenados[:3], start=1):
        print(f'{i}. {datos['nombre']} "{nickname} - Puntos: {datos['puntos']}')
    # Mostrar el peor puntaje (el último de la lista ordenada)
    peorJugador = jugadoresOrdenados[-1]
    print('\n----- Peor Puntaje -----')
    print(f'{peorJugador[1]['nombre']} "{peorJugador[0]}" - Puntos: {peorJugador[1]['puntos']}')
    ut.pausar()

def viewStatsIA(origin):
    # Ordenamos los jugadores por la cantidad de derrotas contra la IA en orden descendente (de mayor a menor)
    jugadores_ordenados = sorted(origin.items(), key=lambda item: item[1]['loseIA'], reverse=True)
    print("Jugadores con más derrotas contra la IA:\n")
    for nickname, datos in jugadores_ordenados:
        print(f'Jugador: {datos['nombre']} "{nickname}" - Derrotas contra la IA: {datos['loseIA']}')
    # Definimos como calcular el promedio
    totalVictorias = 0
    totalJugadores = len(origin) # Total de jugadores registrados
    for nickname, datos in origin.items():
        totalVictorias += datos['winIA']
    # Calculamos el promedio
    if totalJugadores > 0:
        promedio = totalVictorias/totalJugadores
    else:
        promedio = 0
    print(f'\nPromedio de victorias contra la IA entre los jugadores: {promedio}')
    ut.pausar()