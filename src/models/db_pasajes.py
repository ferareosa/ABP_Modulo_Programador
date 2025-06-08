from datetime import datetime, timedelta
from ..types import Pasaje
from ..types import Pasaje_completo
from .scripts import ejecutar_query
from ..utils import consola_rich as consola

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
        consola.error("No hay pasajes registrados.")
        return

    consola.mostrar_tabla(
        titulo="Registro de Pasajes",
        columnas=("ID Venta", "CUIT", "Destino", "Fecha Venta", "Estado", "Costo Total"),
        filas=[
            [
                p["id_venta"],
                p["cuit"],
                p["id_destino"],
                p["fecha_venta"],
                "[info]Activo[/info]" if p["estado"] else "[error]Inactivo[/error]",
                f"${p['costo_total']:.2f}"
            ]
            for p in pasajes
        ]
    )

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
    consola.info("Pasaje comprado con éxito.")

def cancelar_pasaje(id_pasaje: int) -> None:
    """
    Cancela un pasaje dado su ID, si no han pasado más de 60 días desde la compra.

    Args:
        id_pasaje (int): ID del pasaje.
    """
    query = "SELECT fecha_venta FROM Pasaje WHERE id_venta = %s AND estado = TRUE"
    resultado = ejecutar_query(query, (id_pasaje,), fetch=True)

    if not resultado:
        consola.error(f"Pasaje con ID {id_pasaje} no encontrado o ya cancelado.")
        return

    fecha_venta_str = resultado[0]["fecha_venta"]
    try:
        fecha_venta = datetime.strptime(fecha_venta_str, "%d/%m/%Y")
    except ValueError:
        consola.error("Formato de fecha inválido en la base de datos.")
        return

    if datetime.now() > fecha_venta + timedelta(days=60):
        consola.error("El pasaje no puede ser cancelado. Ha pasado el plazo de 60 días.")
        return

    update_query = "UPDATE Pasaje SET estado = FALSE WHERE id_venta = %s"
    ejecutar_query(update_query, (id_pasaje,))
    consola.info(f"Pasaje con ID {id_pasaje} cancelado con éxito.")

def obtener_pasaje(id_venta: int)->Pasaje_completo | None:
    """
    Obtiene el pasaje desde la base de datos mediante una consulta multitabla.

    Returns:
        Pasaje_completo : Pasaje como diccionario.
    """
    query = """
    SELECT
    p.id_venta,
    p.fecha_venta,
    p.estado,
    p.costo_total,
    c.cuit,
    c.razon_social,
    d.ciudad,
    d.pais
    FROM Pasaje p
    JOIN Cliente c ON p.cuit = c.cuit
    JOIN Destino d ON p.id_destino = d.id_destino
    WHERE id_venta = %s;
    
    """
    [pasaje] = ejecutar_query(query, (id_venta,), fetch=True) or None
    return pasaje