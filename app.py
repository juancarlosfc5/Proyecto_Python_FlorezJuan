import modules.core as cr
import modules.games as gm
import modules.menu as m
import modules.messages as msg
import modules.players as pl
import modules.stats as st
import modules.utils as ut

if (__name__ == '__main__'):
    origin = {} # Diccionario base
    cr.MY_DATABASE='data/origin.json' # Establecer ruta del archivo json
    cr.checkFile(origin) # Verificacion archivo json
    isApp = True
    while isApp:
        ut.borrar()
        print(m.menu) # Imprimir menu
        try:
            opcion = int(input(': ')) # Solicitar al usuario que escoja la opcion
        except ValueError:
            print(msg.errorData) # Validacion al no insertar un entero
            ut.pausar()
        else:
            match opcion:
                case 1: # Crear usuario
                    pl.addPlayer(origin)
                case 2: # Partida 1 vs 1
                    gm.juego1vs1(origin)
                case 3: # Partida 1 vs IA
                    gm.juegoIA(origin)
                case 4: # Estadisticas vs IA
                    st.viewStatsIA(origin)
                case 5: # Tabla de puntos 1vs1
                    st.viewStats1vs1(origin)
                case 6: # Salir
                    isApp = ut.validarSalida(msg.salida)
                case _: # Validacion al insertar una opcion incorrecta
                    print(msg.errorOpcion)
                    ut.pausar()