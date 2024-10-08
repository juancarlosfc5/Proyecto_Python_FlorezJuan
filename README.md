# Proyecto_Python_FlorezJuan
Filtro 1. Python - Desarrollo de un juego denominado "The Chachipun" (también conocido como piedra, papel o tijera) que permite enfrentarse entre jugadores y contra la IA, el juego continua hasta que un jugador gane 3 rondas, cabe aclarar que si algun jugador gana 2 rondas consecutivas se le asignara un escudo que será su protección la próxima vez que pierda.
-------- APP -------
Dentro de _app_ se establece el main del proyecto por lo tanto se importan todos los modulos (core, games, menu, messages, players, stats y utils) para tener acceso a cada una de las funciones creadas, adicionalmente, se define el diccionario principal _origin_ el cual recibira la información de los jugadores (nombre, nickname y estadisticas) junto con la llamada de MY_DATABASE en el archivo origin.json en la carpeta data y se realiza el checkfile desde el core para verificar que el archivo existe y cargue los datos o sino que cree el archivo. Luego, se establece el ciclo while con isApp para que el programa permanezca en ejecución hasta que el usuario decida salir, para esto se limpia la pantalla y se imprime el menu llamando el texto del modulo menu, a continuacion se le solicita al usuario que ingrese la opcion a la que desea acceder y se verifica con un try para que solo sean ingresados datos enteros, posteriormente, se establece el match con el fin de acceder a cada funcion del menu (Crear usuario, Partida 1vs1, Partida 1vsIA, Estadistica vs IA, Tabla de puntos 1 vs 1 y Salir), se aclara que la opcion salir pedira confirmar al usuario si esta seguro de la decisión. Finalmente, el case any (_:) envia un mensaje de error ya que si bien se ingreso un entero no se encuentra dentro de las opciones del match.
-------- CORE -------
Dentro del _core_ se importa el sistema operativo y el json con el fin de definir las funciones NewFile para crear el archivo, ReadFile para leer el archivo json almacenado, checkFile para verificar si el archivo existe lo lea y si no existe lo cree y AddData para guardar la información de los jugadores en cuanto a la creacion de usuario (nombre y nickname) y estadisticas de juego (puntos, win, lose, winIA y loseIA).
-------- UTILS -------
Dentro de _utils_ se crean las funciones para borrar y pausar pantalla teniendo en cuenta el sistema operativo para no tener errores al cambiar entre windows y linux, adicionalmente, se crea la funcion validarSalida para establecer la pregunta de validacion al usuario al querer abandonar el programa.
-------- MENU -------
Dentro de _menu_ se crea el menu principal a importar en el match de _app_.
-------- MESSAGES -------
Dentro de _messages_ se crean los mensajes principales a importar en los modulos de acuerdo a la necesidad del programa.
-------- PLAYERS -------
Dentro de _players_ se importan los modulos necesarios (utils para borrar y pausar, core para guardar información y msg para enviar mensajes al usuario), seguido se estructura el diccionario players vacio para que conservara la estructura de datos que se desea almacenar para cada jugador (nombre, nickname, puntos, win, lose, winIA y loseIA), posteriormente, se crea la funcion addPlayer para crear los usuarios iniciado con generar una copia del diccionario players vacio con la funcion copy.deepcopy como newPlayer, posteriormente, se solicita el nombre del usuario y se crea un ciclo while para validar que el nickname no se encuentre registrado previamente por lo tanto se busca el nickname en origin y si existe se imprime el mensaje de error y se solicita nuevamente el nickname hasta tanto ingrese un nickname unico, una vez se logra esto se inserta el nombre y el nickname dentro de newPlayer y luego se almacena el diccionario newPlayer con el nickname como llave dentro del diccionario principal origin. Finalmente, se usa la función AddData del core para almacenar el resgistro en el archivo origin.json.
-------- GAMES -------
Dentro de _games_ se importan los modulos necesarios (random con el fin de que la IA seleccione aleatoriamente una opción, utils para borrar y pausar, core para guardar información y msg para enviar mensajes al usuario), se inicia cargando las opciones disponibles para el juego (piedra, papel o tijera).
_1vsIA_
Seguido se establece la función _rondaIA_ en donde la variable eleccionIA usa la funcion random.choice(opciones) para que se seleccione aleatoriamente la eleccion por parte de la maquina, luego se solicita ingresar la variable eleccionJugador y se realiza la validación con el while para que si no se encuentra dentro de las opciones el dato ingresado solicite ingresar uno nuevo hasta que sea correcto, luego se borra la pantalla y se muestran las elecciones del jugador y la maquina y se valida con el if si fue un empate cuando las elecciones son iguales retornando 'empate', en el elif se vadida si gana el jugador ya que se pone la condicion de comparacion entre eleccionJugador _y_ eleccionIA, siguiendo las instrucciones de que piedra vence tijera, tijera vence papel y papel vence piedra con un condicional _o_ entre cada una de estas 3 retornando 'jugador', para el caso else al no ganar el jugador debe ganar la IA por lo que se retorna directamente 'ia', con esta funcion se logra definir como se ejecutara cada ronda del juego vs IA.
Posteriormente, se establece la función _juegoIA_ en donde se inicializan los contadores en 0 (rondasJugador, rondasIA, contadorJugador y contadorIA) y los escudos en False (escudoJugador y escudoIA) y la bandera de isJuegoIA para determinar el cierre del bluce while de la partida, el while inicia solicitando al usuario que ingrese el nickname del jugador de la partida, por lo que se ingresa el condicional if para verificar que el haya sido creado si no es asi indicara un mensaje de error y retornara al menu principal para que cree el usuario con el break, luego en el else se da la bienvenida a la partida y se inicia el while hasta que rondasJugador _o_ rondasIA sea igual a 3 y se llama recursivamente la funcion rondaIA, teniendo en cuenta que esta funcion retorna un valor (empate, jugador o ia) se establece lo que se debe ejecutar de acuerdo a cada condicion con un if, primero para el caso que el jugador gano la ronda se sumara 1 al contadorJugador y se reinicia en 0 el contadorIA, luego se evalua si el jugador ha ganado las 2 rondas consecutivas (contadorJugador == 2) para asignar el escudo (escudoJugador = True), despues, se crea otro if para validar la victoria pues se inicia verificando si el contrincante (IA) cuenta con escudo si es asi se rompe (pasa de True a False) pero no suma la ronda ganada del jugador pues lo protegio para el caso contrario else si el oponente no cuenta con escudo se suma 1 a la rondasJugador y se reinicia el ciclo, para el caso en que gane la 'ia' se ejecuta de la misma manera el codigo pues se suma 1 al contadorIA se reinicia el contadorJugador a 0 se verifica si gano 2 rondas consecutivas y se activa el escudo en True, luego con el siguiente if se verifica que el jugador tenga escudo activo si lo tiene lo rompe para protegerlo y si no suma 1 a rondasIA, finalmente, en la ultima condicion 'empate' se realiza el reinicio de los dos contadores del jugador y la IA a 0 pues no sería una victoria consecutiva si se dio un empate despues de una victoria, finalmente, con un if cuando rondasJugador sea igual a 3 se almacena la victoria en la llave winIA y se usa AddData para guardar los datos en origin.json y se cierre el bucle con isJuegoIA = False, para el caso else sera que la IA gano por lo que se almacena la derrota en la llave loseIA y se usa AddData para guardar los datos en origin.json. Con esto se finaliza la partida vs IA.
_1vs1_
Seguido