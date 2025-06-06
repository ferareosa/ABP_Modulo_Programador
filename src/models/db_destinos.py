from ..types import Destino
from .scripts import ejecutar_query


def obtener_destinos() -> list[Destino]:
    """
    Obtiene todos los destinos desde la base de datos.

    Returns:
        list[Destino]: Lista de destinos como diccionarios.
    """
    query = "SELECT * FROM Destino ORDER BY disponible DESC"
    return ejecutar_query(query, fetch=True) or []


def imprimir_destinos() -> None:
    """
    Imprime la lista de destinos en la consola.
    """
    destinos = obtener_destinos()
    if not destinos:
        print("No hay destinos registrados.")
        return

    for d in destinos:
        print(f"ID: {d['id_destino']} | Ciudad: {d['ciudad']} | País: {d['pais']} | Costo: ${d['costo_base']} | Disponible: {'Si' if d['disponible'] else 'No'}")


def nuevo_destino(destino: Destino) -> None:
    """
    Agrega un nuevo destino a la base de datos.

    Args:
        destino (Destino): Diccionario con los datos del destino.
    """
    if not (isinstance(destino["ciudad"], str) and isinstance(destino["pais"], str) and isinstance(destino["costo_base"], float)):
        print("El destino nuevo no es válido.")
        return

    query = """
        INSERT INTO Destino (ciudad, pais, costo_base, disponible)
        VALUES (%s, %s, %s, TRUE)
    """
    params = (destino["ciudad"], destino["pais"], destino["costo_base"])
    ejecutar_query(query, params)
    print(f"Destino agregado correctamente.")


def obtener_destino(id_destino: str) -> Destino | None:
    """
    Obtiene un destino específico por su ID.

    Args:
        id_destino (str): ID del destino a buscar.

    Returns:
        Destino | None: Diccionario del destino o None si no se encuentra.
    """
    query = "SELECT * FROM Destino WHERE id_destino = %s"
    resultado = ejecutar_query(query, (id_destino,), fetch=True)
    return resultado[0] if resultado else None


def delete_destino(id_destino: str) -> None:
    """
    Elimina un destino por su ID.

    Args:
        id_destino (str): ID del destino a eliminar.
    """
    query = "DELETE FROM Destino WHERE id_destino = %s"
    ejecutar_query(query, (id_destino,))
    print(f"Destino {id_destino} eliminado.")


def alternar_disponibilidad_destino(id_destino: str) -> None:
    """
    Alterna la disponibilidad de un destino.

    Args:
        id_destino (str): ID del destino a modificar.
    """
    destino = obtener_destino(id_destino)
    if not destino:
        print(f"No se encontró un destino con ID {id_destino}.")
        return

    nuevo_estado = not destino["disponible"]
    query = "UPDATE Destino SET disponible = %s WHERE id_destino = %s"
    ejecutar_query(query, (nuevo_estado, id_destino))
    print(f"Disponibilidad del destino {id_destino} actualizada a {'Disponible' if nuevo_estado else 'No disponible'}.")


def es_destino(id_destino: str) -> bool:
    """
    Verifica si existe un destino por su ID.

    Args:
        id_destino (str): ID del destino.

    Returns:
        bool: True si existe, False si no.
    """
    query = "SELECT 1 FROM Destino WHERE id_destino = %s"
    resultado = ejecutar_query(query, (id_destino,), fetch=True)
    return bool(resultado)

def update_destino(destino:Destino)-> None:
    """
    Modifica un cliente de la base de datos por su CUIT.

    Args:
        cuit (int): CUIT del cliente a eliminar.
    """
    if es_destino(destino["id_destino"]):
        query = '''
        UPDATE Destino 
        SET ciudad= %s, pais= %s, costo_base= %s
        WHERE id_destino= %s
        '''
        ejecutar_query(query, (destino["ciudad"], destino["pais"], destino["costo_base"], destino["id_destino"]))
    else:
        nuevo_destino(destino)