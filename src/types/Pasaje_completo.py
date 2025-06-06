from typing import TypedDict
class Pasaje(TypedDict):
    """
    Definición de la estructura de un pasaje completo.
    """
    id_venta:float
    fecha_venta:str
    estado:bool
    costo_total:float
    cuit:int
    razon_social:str
    ciudad:str
    pais:str