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
    return [[" " for _ in range(3)] for _ in range(3)]

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
        print("¡Casilla ocupada! Inténtalo de nuevo.")
        return False


def verificar_ganador(tablero: list[list[str]], jugador: str) -> bool:
    """
    Verifica si el jugador actual ha ganado el juego de tres en raya.

    Parameters
    ----------
    - tablero : list[List[str]]
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
    # Verificar filas y columnas
    for fila in range(3):
        if all(tablero[fila][columna] == jugador for columna in range(3)) or all(tablero[columna][fila] == jugador for columna in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[fila][fila] == jugador for fila in range(3)) or all(tablero[fila][2 - fila] == jugador for fila in range(3)):
        return True

    return False
  

if __name__ == "__main__":
    tablero = crear_tablero()
    jugadores = ["X", "O"]
    turno = 0

    for _ in range(9):
        imprimir_tablero(tablero)

        jugador_actual = jugadores[turno % 2]
        print(f"Turno del jugador {jugador_actual}")

        fila = int(input("Ingresa el número de fila (0, 1, 2): "))
        columna = int(input("Ingresa el número de columna (0, 1, 2): "))

        if 0 <= fila < 3 and 0 <= columna < 3:
            if realizar_jugada(tablero, fila, columna, jugador_actual):
                if verificar_ganador(tablero, jugador_actual):
                    imprimir_tablero(tablero)
                    print(f"¡El jugador {jugador_actual} ha ganado!")
                elif all(tablero[i][j] != " " for i in range(3) for j in range(3)):
                    imprimir_tablero(tablero)
                    print("¡Es un empate!")
                turno += 1
        else:
            print("¡Posición inválida! Inténtalo de nuevo.")

    imprimir_tablero(tablero)
    print("El juego ha terminado. ¡Es un empate!")