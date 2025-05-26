from typing import TypedDict
class Cliente(TypedDict):
    """
    Definición de la estructura de un cliente.
    """
    cuit: int
    razon_social: str
    email: str