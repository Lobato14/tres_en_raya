import random
# Total de jugadas en el tres en raya
TOTALTURNOS = 9
# Dimension 3x3 del tres en raya
DIMENSION = 3

def menu() -> str:
    print("-----¡¡¡BIENVENIDOS AL TRES EN RAYA!!!--------\n\n" +
          "1. Jugador vs Jugador\n"+
          "2. Jugador vs Maquina\n"+
          "3. Salir del tres en raya\n")
    return input("Elija la una de las siguientes opciones: ")

def imprimir_tablero(tablero: list[list[str]]) -> None:
    """
    Imprime el tablero del juego de tres en raya en la consola.

    Parameters
    ----------
    - tablero : list[list[str]]
        Una lista de listas que representa el estado actual del tablero. 
        Cada elemento de la lista interna puede ser "X", "O" o " ".

    Returns
    -------
    - None
    """
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def crear_tablero() -> list[list[str]]:
    """
    Crea un tablero vacío para el juego de tres en raya.

    Returns
    -------

    - list[list[str]]: Un tablero vacío representado como una lista de listas.
      Cada elemento de la lista interna es una cadena que puede ser "X", "O" o " ".
    """
    return [[" " for _ in range(DIMENSION)] for _ in range(DIMENSION)]

def realizar_jugada(tablero: list[list[str]], fila: int, columna: int, jugador: str) -> bool:
    """
    Realiza una jugada en el juego de tres en raya, colocando el símbolo del jugador 
    en la posición especificada.

    Parameters
    ----------
    - tablero : list[list[str]]
        El tablero actual del juego representado como una lista de listas. 
        Cada elemento de la lista interna es una cadena que puede ser "X", "O" o " ".

    - fila : int
        El número de fila en el tablero donde se realizará la jugada.
    - columna : int
        El número de columna en el tablero donde se realizará la jugada.
    - jugador : str
        El símbolo del jugador ("X" o "O") que realizará la jugada.

    Returns
    -------
    - bool: 
        True si la jugada se realizó con éxito (la casilla estaba vacía), 
        False si la casilla ya estaba ocupada.
    """
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
        return True
    else:
        return False

def realizar_jugada_maquina(tablero, jugador_maquina):
    # Encuentra todas las posiciones vacías en el tablero
    posiciones_disponibles = [(fila, columna) for fila in range(DIMENSION) for columna in range(DIMENSION) if tablero[fila][columna] == " "]

    if posiciones_disponibles:
        # Elije una posición aleatoria de las disponibles
        fila, columna = random.choice(posiciones_disponibles)
        realizar_jugada(tablero, fila, columna, jugador_maquina)
        print(f"La máquina ha realizado su jugada en la fila {fila}, columna {columna}.")
        return fila, columna
    else:
        return None


def hay_ganador(tablero: list[list[str]], jugador: str) -> bool:
    """
    Verifica si el jugador actual ha ganado el juego de tres en raya.

    Parameters
    ----------
    - tablero : list[list[str]]
        El tablero actual del juego representado como una lista de listas.
        Cada elemento de la lista interna es una cadena que puede ser "X", "O" o " ".

    - jugador : str
        El símbolo del jugador ("X" o "O") que se está verificando para determinar 
        si ha ganado.

    Returns
    -------
    - bool: 
        True si el jugador ha ganado, False en caso contrario.
    """
    encontrado = False
    
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(DIMENSION)) or all(tablero[i][(DIMENSION -1) - i] == jugador for i in range(DIMENSION)):
        encontrado = True 
    # Verificar filas y columnas
    contador = 0  
    while not encontrado and contador < DIMENSION:
        if all( tablero[contador][columna] == jugador for columna in range(DIMENSION)) or all(tablero[fila][contador] == jugador for fila in range(DIMENSION)):
            encontrado = True
        contador += 1
    return encontrado 

def obtener_entrada_numero(mensaje: str) -> int:
    """
    Solicita al usuario un número mediante un mensaje y asegura que la entrada sea un número entero válido.

    Parameters
    ----------
    - mensaje : str
        El mensaje que se mostrará al usuario para solicitar la entrada.

    Returns
    -------
    - int: 
        El número entero ingresado por el usuario.
    """
    entrada_valida = False
    while not entrada_valida:
        entrada = input(mensaje)
        if entrada.isdigit():
            entrada_valida = True
        else:
            print("¡Error! Ingresa un número válido.")
    
    return int(entrada)

def obtener_entrada_simbolo(mensaje: str) -> str:
    """
    Solicita al usuario un símbolo ("X" o "O") mediante un mensaje y asegura que la entrada sea válida.

    Parameters
    ----------
    - mensaje : str
        El mensaje que se mostrará al usuario para solicitar la entrada.

    Returns
    -------
    - str: 
        El símbolo ingresado por el usuario ("X" o "O").
    """
    entrada_valida = False

    while not entrada_valida:
        entrada = input(mensaje).upper()
        if entrada in ["X", "O"]:
            entrada_valida = True
        else:
            print("¡Error! Ingresa un símbolo válido (X o O).")
    return entrada

def pedir_posicion():
    fila = obtener_entrada_numero("Ingresa el número de fila (0, 1, 2): ")
    columna = obtener_entrada_numero("Ingresa el número de columna (0, 1, 2): ")

    while not (0 <= fila < 3 and 0 <= columna < 3):
        print("¡Posición inválida! Inténtalo de nuevo.")
        fila = obtener_entrada_numero("Ingresa el número de fila (0, 1, 2): ")
        columna = obtener_entrada_numero("Ingresa el número de columna (0, 1, 2): ")
    return fila,columna

def turno_jugador(jugadores, turno):
    return jugadores[turno % 2]

def elegir_jugador():
    return input("Elige el jugador O o el jugador X: ").lower()

if __name__ == "__main__":

    opcion = menu()
    
    while opcion != "3":
        if opcion == "1":

            tablero = crear_tablero()
            jugadores = ["X", "O"]
            turno = 1
            juego_terminado = False
            jugar_nuevamente = True

            while jugar_nuevamente:
                while not juego_terminado:

                    imprimir_tablero(tablero)

                    jugador_actual = turno_jugador(jugadores, turno)
                    print(f"Turno del jugador {jugador_actual}")

                    fila, columna = pedir_posicion()

                    if realizar_jugada(tablero, fila, columna, jugador_actual):
                        if hay_ganador(tablero, jugador_actual):
                            imprimir_tablero(tablero)
                            print(f"¡El jugador {jugador_actual} ha ganado!")
                            juego_terminado = True
                        elif turno == TOTALTURNOS:
                            imprimir_tablero(tablero)
                            print("¡Es un empate!")
                            juego_terminado = True
                        turno += 1
                    else:
                        print("Casilla ocupada!!")

                respuesta = input("¿Quieres jugar otra vez? (si/no): ").lower()
                jugar_nuevamente = (respuesta == "si")
        
        elif opcion == "2":
            
            jugador_usuario = obtener_entrada_simbolo("Elige el jugador O o el jugador X: ")
            jugador_maquina = "X" if jugador_usuario == "O" else "O"

            while jugar_nuevamente:
                while not juego_terminado:
                    imprimir_tablero(tablero)

                    jugador_actual = turno_jugador(jugadores, turno)
                    print(f"Turno del jugador {jugador_actual}")

                    if jugador_actual == jugador_usuario:

                        fila, columna = pedir_posicion()

                        if realizar_jugada(tablero, fila, columna, jugador_actual):
                            if hay_ganador(tablero, jugador_actual):
                                imprimir_tablero(tablero)
                                print(f"¡El jugador {jugador_actual} ha ganado!")
                                juego_terminado = True
                            elif turno == TOTALTURNOS:
                                imprimir_tablero(tablero)
                                print("¡Es un empate!")
                                juego_terminado = True
                            turno += 1
                        else:
                            print("Casilla ocupada!!")
                    else:
                        
                        jugada_maquina = realizar_jugada_maquina(tablero, jugador_maquina)

                        if jugada_maquina:
                            
                            fila_maquina, columna_maquina = jugada_maquina
                            print(f"La máquina ha realizado su jugada en la fila {fila_maquina}, columna {columna_maquina}.")
                            
                            if hay_ganador(tablero, jugador_maquina):
                                imprimir_tablero(tablero)
                                print(f"¡La máquina ha ganado!")
                                juego_terminado = True
                            elif turno == TOTALTURNOS:
                                imprimir_tablero(tablero)
                                print("¡Es un empate!")
                                juego_terminado = True
                            turno += 1
                        else:
                            print("El tablero está lleno. ¡Es un empate!")

                respuesta = input("¿Quieres jugar otra vez? (si/no): ").lower()
                jugar_nuevamente = (respuesta == "si")
                
        opcion = menu()
    
    print("-----Gracias por jugar. ¡Hasta luego!-------")