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