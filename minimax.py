# ==================================================
# IMPORTACIONES DE LIBRERIAS
# ==================================================

import random # Libreria basica de python para generar numeros aleatorios con un algoritmo
import os     # Nos permite interactuar con el sistema operativo, gestionar archivos, carpetas y "ejecutar comandos del sistema" (que sera su principal uso en este programa)
import time   # Nos permite trabajar con tiempo: fechas, horas, medir cuánto tarda algo, o simplemente "hacer pausas" (que sera su uso principal)


# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------

# FUNCIONES PARA QUE EL PROGRAMA FUNCIONE

# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------


# Funcion 1:
# ---------------------------------------------
# IMPRESION DEL TABLERO DE JUEGO
# ---------------------------------------------

def imprimir_tablero(tablero):
    for fila in tablero: # Recorre cada fila
        print(" ".join(fila))   # Une los elementos de la lista de "filas"
                                # Creando un solo string
                                # con espacios entre ellos y los imprime
                                # Ej: [".", ".", "R", "."] a "". . R .
    print( ) #Separador



# Funcion 2:
# ---------------------------
# LIMPIAR CONSOLA
# ---------------------------

def limpiar_la_consola(): #Vamos a usar esta funcion para darle un toque estetico al juego mejor en la consola y que se pueda apreciar mejor
    # "os.system" nos permite interactuar con el sistema, osea poner codigo dentro del programa que se ejecute en la consola junto al programa
    os.system("cls")
            #DATOS:
                # "system" le dice al sistema operativo "ejecuta esto:"
                # "clear" limpia la consola


# Funcion 3:
# ---------------------------------------------------
# GENERACION DE MOVIMIENTOS RANDOMS PARA LOS JUGADORES
# ---------------------------------------------------

def nuevo_movimiento(tablero, posicion, simbolo, movimientos):

    while True: # Bucle infinito de busqueda de un movimiento randoms valido
        direccion = random.choice(list(movimientos.values() )) # Toma una direccion randoms

        # Nuevo movimiento
        nueva_fila    = posicion[0] + direccion[0]
        nueva_columna = posicion[1] + direccion[1]
        
        # pone el simbolo en el tablero para analizarlo
        simbolo_en_destino = tablero[nueva_fila][nueva_columna]

        # REGLA CLAVE: Un movimiento es válido si el destino no es un muro.
        # Las reglas de captura/escape se manejan en el bucle principal.
        if simbolo_en_destino != "#":
            # REGLA EXTRA: El ratón no puede ir a la casilla del gato.
            if simbolo == "🐭" and simbolo_en_destino == "🐱":
                continue # Vuelve a intentarlo, este movimiento no es válido para el ratón.
            break

    # Actualizacion del tablero
    tablero[posicion[0]][posicion[1]] = "." # Posicion actual la reemplaza
    tablero[nueva_fila][nueva_columna] = simbolo # Pone el simbolo en la nueva posicion del tablero

    # Retorna ese valor
    return (nueva_fila, nueva_columna)

# Funcion 4:
# ---------------------------------------------
# EVALUAR ESTADO DEL JUEGO Y SU VALOR
# ---------------------------------------------

# Esta función evalúa qué tan buena o mala es una posición del juego para el ratón
def evaluar_estado_simple(posicion_raton, posicion_gato, cueva):
    """
    Evalúa el estado del juego con una lógica simple.
    Un valor más alto es mejor para el ratón (Maximizador).
    """
    # Si el ratón escapa, es la victoria máxima.
    if posicion_raton == cueva:
        return 10000  # Valor muy alto

    # Si el gato atrapa al ratón, es la derrota máxima.
    if posicion_raton == posicion_gato:
        return -10000 # Valor muy bajo

    # Qué tan lejos está el ratón de la cueva (MALO para el ratón))
    distancia_cueva = abs(posicion_raton[0] - cueva[0]) + abs(posicion_raton[1] - cueva[1])
    
    # Qué tan lejos está el gato del ratón (BUENO para el ratón)
    distancia_gato = abs(posicion_raton[0] - posicion_gato[0]) + abs(posicion_raton[1] - posicion_gato[1])
    
    # El valor es la distancia que el ratón tiene que huir del gato,
    # menos la distancia que le falta para llegar a la cueva.
    # El ratón quiere que este valor sea lo más grande posible.
    valor = distancia_gato - distancia_cueva
    
    return valor

# Funcion 5:
# --------------
# MINIMAX
# --------------

def minimax_simple(posicion_raton, posicion_gato, cueva, profundidad, es_turno_del_gato, diccionario_movimientos, tablero):
    """
    Algoritmo Minimax recursivo y simple.
    - `profundidad`: Cuántos turnos mira hacia adelante.
    - `es_turno_del_gato`: True si es el turno del gato, False si es del ratón.
    """

    # Se acabaron los turnos a simular (profundidad == 0) El juego terminó (ratón escapó o fue capturado)
    if profundidad == 0 or posicion_raton == cueva or posicion_raton == posicion_gato:
        return evaluar_estado_simple(posicion_raton, posicion_gato, cueva) # Retorna la puntuaacion de esa posicion

    # Si es el turno del GATO (Minimizador)
    if es_turno_del_gato:
        # infinito +
        mejor_valor = float('inf')  # El gato busca el valor más bajo
        for movimiento in diccionario_movimientos.values():
            # calcula la nueva posicion
            nueva_posicion_gato = (posicion_gato[0] + movimiento[0], posicion_gato[1] + movimiento[1])

            # Solo consideramos movimientos válidos para el GATO
            # Se puede mover a un espacio vacío, al ratón (captura), o a la cueva.
            if tablero[nueva_posicion_gato[0]][nueva_posicion_gato[1]] != "#":
                
                # Simular el movimiento del gato
                if nueva_posicion_gato == posicion_raton:
                    # Si el gato atrapa al ratón, es una victoria para el gato.
                    valor = -1000
                else:
                    # Llamada recursiva: el siguiente turno es del ratón
                    valor = minimax_simple(posicion_raton, nueva_posicion_gato, cueva, profundidad - 1, False, diccionario_movimientos, tablero)
                
                mejor_valor = min(mejor_valor, valor)

        return mejor_valor

    # Si es el turno del RATÓN (Maximizador)
    else:
        # infinito -
        mejor_valor = float('-inf') # El ratón busca el valor más alto
        for movimiento in diccionario_movimientos.values():
            nueva_posicion_raton = (posicion_raton[0] + movimiento[0], posicion_raton[1] + movimiento[1])
            
            # Solo consideramos movimientos válidos para el RATÓN
            # El ratón solo puede moverse a una posición vacía o a la cueva, pero no a la posición del gato.
            if tablero[nueva_posicion_raton[0]][nueva_posicion_raton[1]] != "#" and nueva_posicion_raton != posicion_gato:

                # Simular el movimiento del ratón
                if nueva_posicion_raton == cueva:
                    # Si el ratón llega a la cueva, es una victoria para el ratón.
                    valor = 1000
                else:
                    # Llamada recursiva: el siguiente turno es del gato
                    valor = minimax_simple(nueva_posicion_raton, posicion_gato, cueva, profundidad - 1, True, diccionario_movimientos, tablero)
                
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor

# Funcion 6:
# ---------------------------------------------
# MOVIMIENTOS DE PERSONAJE INTELIGENTES
# ---------------------------------------------

def mover_jugador_ia(tablero, posicion_jugador, posicion_oponente, cueva, es_gato, diccionario_movimientos):
    """
    Usa el algoritmo Minimax para encontrar el mejor movimiento.
    `es_gato`: True si se mueve el gato, False si se mueve el ratón.
    """
    mejor_movimiento = None
    
    # Definimos el valor inicial para buscar.
    if es_gato:
        mejor_valor = float('inf')   # Gato (Min) quiere el valor más bajo
        for movimiento in diccionario_movimientos.values():
            nueva_posicion = (posicion_jugador[0] + movimiento[0], posicion_jugador[1] + movimiento[1])
            
            # Ignorar movimientos que choquen con un muro o la cueva.
            if tablero[nueva_posicion[0]][nueva_posicion[1]] == "#" or nueva_posicion == cueva:
                continue

            # Simular el movimiento y obtener el valor Minimax
            valor = minimax_simple(posicion_oponente, nueva_posicion, cueva, 2, False, diccionario_movimientos, tablero)
            
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = nueva_posicion
    else: # Es el ratón
        mejor_valor = float('-inf')  # Ratón (Max) quiere el valor más alto
        for movimiento in diccionario_movimientos.values():
            nueva_posicion = (posicion_jugador[0] + movimiento[0], posicion_jugador[1] + movimiento[1])
            
            # Ignorar movimientos que choquen con un muro o la posición del gato.
            if tablero[nueva_posicion[0]][nueva_posicion[1]] == "#" or nueva_posicion == posicion_oponente:
                continue

            # Simular el movimiento y obtener el valor Minimax
            valor = minimax_simple(nueva_posicion, posicion_oponente, cueva, 2, True, diccionario_movimientos, tablero)
            
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = nueva_posicion

    # Si no hay un movimiento, el jugador se queda donde está.
    if mejor_movimiento is None:
        return posicion_jugador
    
    # Actualizamos el tablero con el mejor movimiento.
    tablero[posicion_jugador[0]][posicion_jugador[1]] = "."
    if es_gato:
        tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "🐱"
    else:
        tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "🐭"
    
    return mejor_movimiento


# Funcion 7:
# ------------------------------------------------
# INICIA EL JUEGO CON LOS PERSONAJES SIENDO BOTS
# ------------------------------------------------

# Dentro de tu función de bucle de juego:
def prueba_con_ia(tablero, posicion_raton, posicion_gato, cueva, diccionario_movimientos):
    turno = 0
    while True:
        # Limpia la consola, imprime el tablero, imprime y suma el contador, y genera un pequeño retardo en el codigo entre ciclos
        limpiar_la_consola()
        imprimir_tablero(tablero)
        print(f"Turno: {turno + 1}")
        time.sleep(0.2)

        # El ratón se mueve de forma inteligente
        posicion_raton = mover_jugador_ia(tablero, posicion_raton, posicion_gato, cueva, False, diccionario_movimientos)
        
        # El gato se mueve de forma inteligente
        posicion_gato = mover_jugador_ia(tablero, posicion_gato, posicion_raton, cueva, True, diccionario_movimientos)
        
        # Contador de turnos
        turno += 1

        # Condiciones de VICTORIA/DERROTA
        if posicion_raton == cueva:
            # Lógica de victoria del ratón
            break
        elif posicion_raton == posicion_gato:
            # Lógica de victoria del gato
            break



# Funcion 8:
# ----------------------------------------------------------
# SIMULACION INFINITA DE TURNOS CON MOVIMIENTOS ALEATORIOS
# ----------------------------------------------------------

def prueba_compleja(tablero, posicion_raton, posicion_gato, cueva):

    turno = 0
    while True:
        # Contador y impresor de turnos
        print(f"Turno:{turno + 1}")
        turno +=  1
        
        # Crea los movimientos del gato y raton, llamando a la funcion nuevo_movimiento (que seran aleatorios)
        posicion_raton = nuevo_movimiento(tablero, posicion_raton, "🐭", diccionario_movimientos)
        posicion_gato  = nuevo_movimiento(tablero, posicion_gato , "🐱", diccionario_movimientos )

        # Se limpia e imprime el tablero y se crea una pequeña pausa en cada vuelta
        limpiar_la_consola()
        imprimir_tablero(tablero)
        time.sleep(0.2)

        # Condiciones de VICTORIA/DERROTA 
        # Cuando se cumpla laguna se termina el bucle y acaba l prueba
        if posicion_raton == cueva:
            print("EL RATON LOGRO ESCAPAR DEL GATO VICTORIA")
            break
        elif posicion_raton == posicion_gato:
            print("EL GATO ATRAPO AL RATON PERDISTE")
            break


# Funcion 9:
# ---------------------------------------------------
# FUNCION PARA CONTROLAR MANUALMENTE A UN JUGADOR
# ---------------------------------------------------

def jugador_manual(tablero, posicion, simbolo):

    # INDICACIONES DE MOVIMIENTOS PARA LA PERSONA QUE JUEGUE
    print("Seleccione su movimiento")
    print("Lea las instrucciones con atencion")
    print("W. Arriba, S. abajo. A. Izquierda. D. Derecha")
    print("Q. Arriba izquierda, E. Arriba derecha, Z. Abajo izquierda, C. Abajo Derecha")
    
    while True: # Blucle permanente hasta que el jugador haga un movimiento valido

        tecla         = input("Eliga su direccion").lower()  # Pedimos la tecla del movimineto
        direccion     = diccionario_movimientos.get( tecla ) # Buscamos en el diccionario el valor de la llave abierta con la tecla
        
        # Validar si la tecla es valida
        if not direccion: # "Si la tecla no corresponde con una clave del diccionrio"
            print("Tecla no valida, inserte una tecla valida")
            continue #  Volvemos a reiniciar hasta tener un movimieno valido

        # Se obtiene la nueva posicion, sumando la posicion actual mas el moviento a realizar
        nueva_fila    = posicion[0] + direccion[0]
        nueva_columna = posicion[1] + direccion[1]

        # Obtenemos el símbolo en el destino
        simbolo_en_destino = tablero[nueva_fila][nueva_columna]

        # Vamos a darle el valor falso a el movimiento para analizarlo
        movimiento_valido = False

        # Validamos si la posicion esta vacia y es valida
        if simbolo == "🐭": # "Si el movimiento es del raton"
            # El ratón puede moverse a un espacio vacío o a la cueva
            if simbolo_en_destino == "." or simbolo_en_destino == "🏠":
                movimiento_valido = True
            else: # SI no es un movimiento valdido...
                print("El ratón no puede moverse a esa posición. Hay un muro o el gato.")
        
        # Si el jugador es el gato...
        elif simbolo == "🐱":
            # El gato puede moverse a un espacio vacío o al ratón.
            if simbolo_en_destino == "." or simbolo_en_destino == "🐭":
                movimiento_valido = True
            else: # Si no es un movimiento valido...
                print("El gato no puede moverse a esa posición. Hay un muro o la cueva.")

        if movimiento_valido:
            break
        else:
            print("Hay un muro o obstaculo bloqueando esa direccion")
    
    
    limpiar_la_consola()                         # Limpiamos la consola para que se vea facha
    tablero[posicion[0]][posicion[1]] = "."      # Reescribimos la posicion anterios
    tablero[nueva_fila][nueva_columna] = simbolo # Colocamos al jugador
    imprimir_tablero(tablero)                    # Imprimimos el tablero actualizado
    time.sleep(0.2)                              # Mini pausa para mejorar como se ve el programa

    return (nueva_fila, nueva_columna) # Devolvemos la nueva posicion


# Funcion 10:
# ---------------------------------------------------
# JUEGO CON JUGADOR MANUAL Y RANDOMS
# ---------------------------------------------------

def prueba_compleja_manual(tablero, posicion_raton, posicion_gato, cueva):

    turno = 0
    while True:
        # Contador de turnos
        print(f"Turno:{turno + 1}")
        turno +=  1
        
        # Se generan las posiciones de los jugadores, con la diferencia de que puedes controlar a uno de los jugadores, al llamar  ala funcion jugador_manual
        posicion_raton = jugador_manual(tablero, posicion_raton, "🐭",)
        posicion_gato  = nuevo_movimiento(tablero, posicion_gato , "🐱", diccionario_movimientos )

        # Se limpia e imprime el tablero, y se genera un pequeño retardo en cada ciclo
        limpiar_la_consola()
        imprimir_tablero(tablero)
        time.sleep(0.2)

        # Condiciones de VICTORIA/DERROTA
        if posicion_raton == cueva:
            print("EL RATON LOGRO ESCAPAR DEL GATO VICTORIA")
            break
        elif posicion_raton == posicion_gato:
            print("EL GATO ATRAPO AL RATON PERDISTE")
            break


# Funcion 11:
# ---------------------------------------------------
# JUEGO CON JUGADOR MANUAL Y BOT
# ---------------------------------------------------

def prueba_compleja_manual_con_bot(tablero, posicion_raton, posicion_gato, cueva):

    turno = 0
    while True:
        # Contador de turnos
        print(f"Turno:{turno + 1}")
        turno += 1
        
        # El ratón se mueve manualmente (jugador humano)
        posicion_raton = jugador_manual(tablero, posicion_raton, "🐭")
        
        # El gato se mueve con la IA (bot)
        posicion_gato  = mover_jugador_ia(tablero, posicion_gato, posicion_raton, cueva, True, diccionario_movimientos)

        # Se limpia e imprime el tablero, y se genera un pequeño retardo en cada ciclo
        limpiar_la_consola( )
        imprimir_tablero(tablero)
        time.sleep(0.2)

        if posicion_raton == cueva:
            print("EL RATON LOGRO ESCAPAR DEL GATO VICTORIA")
            break
        elif posicion_raton == posicion_gato:
            print("EL GATO ATRAPO AL RATON PERDISTE")
            break






# ---------------------------------------------
# BLOQUE PRINCIPAL DE INICIALIZACION DEL JUEGO
# ---------------------------------------------

# Hace que el codigo sea reutilizable
# Mejora la estetica del codigo
# Separa las logicas del juego
# Evita posibles problemas como ejecuciones accidentales


if __name__ == "__main__":

    # ------------------
    # BIENVENIDA
    # ------------------

    print("Bienvenido al loco juego del gato y el raton")
    print() # Genera un espacio entre los textos   

    
    # -----------------------------------
    # CREACION DEL TABLERO DE JUEGO
    # -----------------------------------

    # TAMANHO DEL TABLERO
    while True: # Bluque para solicitar el tamanho del tablero
        # Se pide el ancho y largo
        filas = int(input("Ingrese el numero de filas del tablero"))
        columnas = int(input("ingrese el numero de columnas del tablero"))
        
        # Condicional para romper el bucle si tiene el tamanho minimo es muy pequeño
        if filas >= 10 and columnas >= 10: # "Si las filas y columnas son iguales o mayores que 10 rompe el bucle"
            break
        # Si no lo repite eternamente hasta que el tamanho sea valido
        print("El tablero debe ser de minimo 10x10")


    # ---------------------------------------------
    # CREACION DEL TABLERO VACIO
    # ---------------------------------------------
                #Creacion de columnas y filas del tablero (Divido en 2 partes Interna/Externa)
    tablero = [["." for _ in range(columnas)] for _ in range(filas)]
                #Datos:   
                        # Parte interna (primer corchete): ( Esta parte crea las Columnas Verticales)
                    # _ Es una convencion que significa: "No me importa el valor de la variable solo quiero repetir algo"
                    # ["." for in range(columnas)] Genera una lista de "." repetido tantas veces como columnas hayamos indicado para el tablero
                        
                        # Parte externa (Segundo corchete): ( Esta parte crea las Filas del tablero (La linea horizontal))
                    # [for _ in range (filas)] “Haz tantas filas (Replicando la lista de columnas) como numero de filas le hayas indicado al tablero”.


    # -----------------------------
    # CREACION DE MUROS Y PAREDES
    # -----------------------------

    # MUROS/BORDES/LIMITES
        # Coloca muros "#" en la fila superior e inferior
    for columna in range(columnas):
            #  ( Y; X )
        tablero[0]  [columna]        = "#"
        tablero[filas - 1][columna]  = "#"

        # Coloca muros en las columnas de la derecha e izquierda
    for fila in range(filas):
        #      ( Y  ; X )
        tablero[fila][0]            = "#"
        tablero[fila][columnas - 1] = "#"


    # ------------------------------------------
    # MENU DE LAS POSICIONES DE LOS JUGADORES
    # ------------------------------------------

    print("\nElige las posiciones del Gato 🐱 y al Ratón 🐭:")
    print("1. Raton en esquina y Gato en el centro")
    print("2. Raton en esquina y Gato en esquina opuesta")
    print("3. Posiciones aleatorias")

    posiciones_jugadores = int(input("Opcion: "))


    # 1 Posiciones: Esquina y centro (pacman)
    if posiciones_jugadores == 1:
        posicion_raton = (1, 1) # Raton esquina izquierda
        posicion_gato  = (filas // 2, columnas //2 ) # Gato en el centro 
                        #(Divide a la mitad filas y columnas)
        cueva = (filas - 2, columnas - 2) # la cueva se genera en la esquina opuesta
        tablero[cueva[0]][cueva[1]] = "🏠"

    # 2 Posiciones: Esquinas opuestas
    elif posiciones_jugadores == 2:
        posicion_raton = (1, 1)# Raton esquina izquierda
        posicion_gato  = (filas - 2, columnas - 2) # Gato ezquina opuesta
        cueva = (1, columnas - 2) # Genera la cueva cerca del gato
        tablero[cueva[0]][cueva[1]] = "🏠"

    # 3 Posiciones: Aleatorias
    elif posiciones_jugadores == 3:

        # Creacion de la posicion aleatoria del raton
        while True: # Bucle infinito que crea una posicion random para el raton y verifica si es valida
            posicion_raton = (random.randint(1, filas - 2), random.randint(1, columnas - 2))
            if tablero[posicion_raton[0]][posicion_raton[1]] == ".":
                break


        # Creacion de la posicion aleatoria del gato
        while True: #Bucle infinito que crea una posicion random y verifica si es valida y diferente al raton
            posicion_gato = (random.randint(1, filas - 2), random.randint(1, columnas - 2))
            if tablero[posicion_gato[0]][posicion_gato[1]] == "." and posicion_gato != posicion_raton:
                break

        # Creacion de la posicion aleatoria de la cueva 
        while True: #Bucle infinito que crea una posicion random para la cueva y verifica si es valida y diferente al raton y gato
            cueva = (random.randint(1, filas - 2), random.randint(1, columnas - 2))
            if tablero[cueva[0]][cueva[1]] == "." and cueva != posicion_gato and cueva != posicion_raton:
                break
        
        tablero[cueva[0]][cueva[1]] = "🏠" # Pone la cueva y su simbolo en la posicion que le corresponda en el mapa


    # Eleccion no valida
    else: # Se eligio una opcion incorrecta, por tanto se elige una fija por defecto
        print("Opcion invalida, posicion de gato en el centro por defecto")
        posicion_raton = (1, 1) # Raton esquina izquierda
        posicion_gato  = (filas // 2, columnas //2 ) # Gato en el centro 
        cueva = (filas - 2, columnas - 2)
        tablero[cueva[0]][cueva[1]] = "🏠"


    # ---------------------------------------------------
    # INTRODUCION DEL GATO Y RATON AL TABLERO
    # ---------------------------------------------------

            # Fila Y            # Columna X
    tablero[posicion_raton[0]] [posicion_raton[1]] = "🐭"
    tablero[posicion_gato[0] ] [posicion_gato[1]]  = "🐱"
    # Reemplazan la celda vacia (representada con ".") con el simbolo del jugador


    # ---------------------------------------------------
    # MOVIMIENTOS DE LOS JUGADORES
    # ---------------------------------------------------

    # Diccionario Delta con los movimientos de los jugadores (Delta = cambio/diferencia)
    diccionario_movimientos = {
    # tecla| (Y  ; X) |movimienot a realizar|
        "w": (-1,  0), # Arriba
        "s": (1 ,  0), # Abajo
        "a": (0 , -1), # Izquierda
        "d": (0 ,  1), # Derecha
        "q": (-1, -1), # Arriba izquierda
        "e": (-1,  1), # Arriba derecha
        "z": (1,  -1), # Abajo izquierda
        "c": (1,   1), # Abajo derecha

    }

    # ------------------------
    # INICIO DEL JUEGO
    # ------------------------

    print("TABLERO INICIAL")
    imprimir_tablero(tablero) # Llamamos/Inciamos la funcion para mostrar el tablero en la consola


    # ----------------------------------------------------
    # LLAMADOS A LAS FUNCIONES PARA QUE FUNCIONEN
    # ----------------------------------------------------
    # Al irlas ejecutando en este orden podremos ver la evolucion de la capacidad de movimiento o inteligencia de los personajes
    # Desde que sean completamente tontos (aleatorios) hasta inteligentes (minimax) y permitiendonos poder controlarlos tambien de forma manual

    #-1:
    # Llama a esta función para empezar el juego
    #prueba_con_ia(tablero, posicion_raton, posicion_gato, cueva, diccionario_movimientos)

    #-2:
    #prueba_compleja_manual(tablero, posicion_raton, posicion_gato, cueva)

    #-3:
    prueba_compleja(tablero, posicion_raton, posicion_gato, cueva)

    #-4:
    #prueba_compleja_manual_con_bot(tablero, posicion_raton, posicion_gato, cueva)

