import modules.utils as ut
import modules.core as cr
import modules.messages as msg
import modules.menu as m
import modules.players as pl

if (__name__ == '__main__'):
    origin ={}
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
                case 1: #Crear usuario
                    pl.addPlayer(origin)
                case 2: #Partida 1 vs 1
                    ut.borrar()
                case 3: #Partida 1 vs IA
                    ut.borrar()
                case 4: #Estadisticas generales
                    ut.borrar()
                case 5: #Tabla de puntos
                    ut.borrar()
                case 6: #Salir
                    isApp = ut.validarSalida(msg.salida)
                case _:
                    print(msg.errorOpcion)
                    ut.pausar()