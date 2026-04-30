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
    

        # INICIO DEL JUEGO

        print("TABLERO INICIAL")
        imprimir_tablero(tablero) # Llamamos/Inciamos la funcion para mostrar el tablero en la consola