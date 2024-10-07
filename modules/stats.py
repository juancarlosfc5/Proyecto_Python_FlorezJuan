def viewStats(origin):
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