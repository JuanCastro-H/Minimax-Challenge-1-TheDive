# IMPORTACIONES DE LIBRERIAS
import random # Libreria basica de python para generar numeros aleatorios con un algoritmo

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