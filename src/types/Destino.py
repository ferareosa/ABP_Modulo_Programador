from typing import TypedDict, NotRequired
class Destino(TypedDict):
    """
    Definición de la estructura de un cliente.
    """
    ciudad: str
    pais: str
    costo_base: float
    disponible: NotRequired[bool]