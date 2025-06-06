from datetime import datetime, timedelta
from ..types import Pasaje
from .scripts import ejecutar_query


def obtener_pasajes() -> list[Pasaje]:
    """
    Obtiene la lista de pasajes desde la base de datos.

    Returns:
        list[Pasaje]: Lista de pasajes como diccionarios.
    """
    query = "SELECT * FROM Pasaje disponible ORDER BY estado DESC"
    return ejecutar_query(query, fetch=True) or []


def imprimir_registro() -> None:
    """
    Imprime la lista de pasajes en la consola.
    """
    pasajes = obtener_pasajes()
    if not pasajes:
        print("No hay pasajes registrados.")
        return

    for p in pasajes:
        print(f"ID Venta: {p['id_venta']} | CUIT: {p['cuit']} | Destino: {p['id_destino']} | Fecha: {p['fecha_venta']} | Estado: {'Activo' if p['estado'] else 'Inactivo'} | Costo: ${p['costo_total']}")


def comprar_pasaje(pasaje: Pasaje) -> None:
    """
    Registra la compra de un pasaje en la base de datos.

    Args:
        pasaje (Pasaje): Diccionario con los datos del pasaje.
    """

    query = """
        INSERT INTO Pasaje (cuit, id_destino, fecha_venta, estado, costo_total)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (
        pasaje["cuit"],
        pasaje["id_destino"],
        pasaje["fecha_venta"], 
        True,
        pasaje["costo_total"]
    )
    ejecutar_query(query, params)
    print("Pasaje comprado con éxito.")

def cancelar_pasaje(id_pasaje: int) -> None:
    """
    Cancela un pasaje dado su ID, si no han pasado más de 60 días desde la compra.

    Args:
        id_pasaje (int): ID del pasaje.
    """
    query = "SELECT fecha_venta FROM Pasaje WHERE id_venta = %s AND estado = TRUE"
    resultado = ejecutar_query(query, (id_pasaje,), fetch=True)

    if not resultado:
        print(f"Pasaje con ID {id_pasaje} no encontrado o ya cancelado.")
        return

    fecha_venta_str = resultado[0]["fecha_venta"]
    try:
        fecha_venta = datetime.strptime(fecha_venta_str, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha inválido en la base de datos.")
        return

    if datetime.now() > fecha_venta + timedelta(days=60):
        print("El pasaje no puede ser cancelado. Ha pasado el plazo de 60 días.")
        return

    update_query = "UPDATE Pasaje SET estado = FALSE WHERE id_venta = %s"
    ejecutar_query(update_query, (id_pasaje,))
    print(f"Pasaje con ID {id_pasaje} cancelado con éxito.")