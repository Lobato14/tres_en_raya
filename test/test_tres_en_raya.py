from src.tres_en_raya import (
    imprimir_tablero,
    crear_tablero,
    realizar_jugada,
    verificar_ganador,
    obtener_entrada_numero,
)

def test_crear_tablero():
    tablero = crear_tablero()
    assert len(tablero) == 3
    assert all(len(fila) == 3 for fila in tablero)
    assert all(all(casilla == " " for casilla in fila) for fila in tablero)

def test_realizar_jugada():
    tablero = crear_tablero()

    # Jugada válida
    assert realizar_jugada(tablero, 0, 0, "X")
    assert tablero[0][0] == "X"

    # Jugada inválida (casilla ocupada)
    assert not realizar_jugada(tablero, 0, 0, "O")
    assert tablero[0][0] == "X"  # No debería cambiar

def test_verificar_ganador():
    tablero = crear_tablero()

    # Ganador en fila
    tablero[0] = ["X", "X", "X"]
    assert verificar_ganador(tablero, "X")

    # Ganador en columna
    tablero = crear_tablero()
    tablero[0][0] = tablero[1][0] = tablero[2][0] = "O"
    assert verificar_ganador(tablero, "O")

    # Ganador en diagonal
    tablero = crear_tablero()
    tablero[0][0] = tablero[1][1] = tablero[2][2] = "X"
    assert verificar_ganador(tablero, "X")

def test_obtener_entrada_numero(monkeypatch):
    # Simula la entrada del usuario
    monkeypatch.setattr("builtins.input", lambda _: "2")

    entrada = obtener_entrada_numero("Ingresa un número: ")
    assert entrada == 2