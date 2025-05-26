from typing import Literal
def dato_ingresado(nombre_dato : str, tipo : Literal["str", "int", "float"]) -> str | int | float | None:
    """
    Esta función solicita al usuario que ingrese una opción y verifica si es válida.
    Si la opción es válida, la devuelve; de lo contrario, muestra un mensaje de error y vuelve a solicitar la entrada.
    """
    
    dato = input(f"Ingresar {nombre_dato}: ")
    if dato and tipo == "str":
        return dato
    elif tipo == "str": return None
    elif tipo == "int":
        try:
            return int(dato)
        except ValueError:
            return None
    elif tipo == "float":
        try:
            return float(dato)
        except ValueError:
            return None
    return None