# IMPORTACIONES DE LIBRERIAS
import random # Libreria basica de python para generar numeros aleatorios con un algoritmo


#---------------------------------------------------

# FUNCIONES PARA QUE EL PROGRAMA FUNCIONE

#---------------------------------------------------


#---------------------------------------------
# IMPRESION DEL TABLERO DE JUEGO
#---------------------------------------------

def imprimir_tablero(tablero):
    for fila in tablero: # Recorre cada fila
        print(" ".join(fila))   # Une los elementos de la lista de "filas"
                                # Creando un solo string
                                # con espacios entre ellos y los imprime
                                # Ej: [".", ".", "R", "."] a "". . R .
    print( ) #Separador



# Funcion : GENERACION DE MOVIMIENTOS RANDOMS PARA LOS JUGADORES


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



# Funcion: EVALUAR ESTADO DEL JUEGO Y SU VALOR


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



# Funcion 4: MINIMAX


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



if __name__ == "__main__":

    # Bienvenida

    print("Bienvenido al loco juego del gato y el raton")
    print() # Genera un espacio entre los textos   

    # CREACION DEL TABLERO DE JUEGO

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



    # CREACION DEL TABLERO
                #Creacion de columnas y filas del tablero (Divido en 2 partes Interna/Externa)
    tablero = [["." for _ in range(columnas)] for _ in range(filas)]
                #Datos:   
                    # Parte interna (primer corchete): ( Esta parte crea las Columnas Verticales)
                    # _ Es una convencion que significa: "No me importa el valor de la variable solo quiero repetir algo"
                    # ["." for in range(columnas)] Genera una lista de "." repetido tantas veces como columnas hayamos indicado para el tablero
                    # Parte externa (Segundo corchete): ( Esta parte crea las Filas del tablero (La linea horizontal))
                    # [for _ in range (filas)] “Haz tantas filas (Replicando la lista de columnas) como numero de filas le hayas indicado al tablero”.



    # CREACION DE MUROS Y PAREDES

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



    # MENU DE LAS POSICIONES DE LOS JUGADORES

    print("\nElige las posiciones del Gato 🐱 y al Ratón 🐭:")
    print("1. Raton en esquina y Gato en el centro")
    print("2. Raton en esquina y Gato en esquina opuesta")
    print("3. Posiciones aleatorias")

    posiciones_jugadores = int(input("Opcion: ")) # Tomamos la opcion que eligio el usuario


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


    # INTRODUCION DEL GATO Y RATON AL TABLERO

            # Fila Y            # Columna X
    tablero[posicion_raton[0]] [posicion_raton[1]] = "🐭"
    tablero[posicion_gato[0] ] [posicion_gato[1]]  = "🐱"
    # Reemplazan la celda vacia (representada con ".") con el simbolo del jugador


    # INICIO DEL JUEGO

    print("TABLERO INICIAL")
    imprimir_tablero(tablero) # Llamamos/Inciamos la funcion para mostrar el tablero en la consola



    # MOVIMIENTOS DE LOS JUGADORES

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
