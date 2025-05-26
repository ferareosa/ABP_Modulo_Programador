from typing import TypedDict
class Pasaje(TypedDict):
    """
    Definición de la estructura de un pasaje.
    """
    id_venta: int
    cuit: int
    id_destino: int
    fecha_venta: str
    estado: bool
    costo_total: float