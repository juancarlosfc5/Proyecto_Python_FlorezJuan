import modules.utils as ut
import modules.core as cr
import modules.messages as msg
import modules.menu as m
import modules.players as pl
import modules.games as gm
import modules.stats as st

if (__name__ == '__main__'):
    origin ={}
    cr.MY_DATABASE='data/origin.json'
    cr.checkFile(origin)
    isApp = True
    while isApp:
        ut.borrar()
        print(m.menu)
        try:
            opcion = int(input(': '))
        except ValueError:
            print(msg.errorData)
            ut.pausar()
        else:
            match opcion:
                case 1: # Crear usuario
                    pl.addPlayer(origin)
                case 2: # Partida 1 vs 1
                    gm.juego1vs1(origin)
                case 3: # Partida 1 vs IA
                    gm.juegoIA(origin)
                case 4: # Estadisticas generales
                    st.viewStatsIA(origin)
                case 5: # Tabla de puntos
                    st.viewStats1vs1(origin)
                case 6: # Salir
                    isApp = ut.validarSalida(msg.salida)
                case _:
                    print(msg.errorOpcion)
                    ut.pausar()