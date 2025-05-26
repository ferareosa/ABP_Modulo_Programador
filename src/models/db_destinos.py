import pandas as pd
from ..types import Destino
from .scripts import cargar_o_crear_csv
from .scripts import guardar_csv
def obtener_destinos()-> pd.DataFrame:
    """
    Obtiene la lista de destinos desde un archivo CSV y la devuelve como un DataFrame de pandas.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de los destinos.
    """
    columnas = ['id_destino','ciudad','pais','costo_base','disponible']
    return cargar_o_crear_csv('models/DB/destinos.csv', columnas)


def guardar_destinos(df_nuevo: pd.DataFrame) -> None:
    """
    Guarda el DataFrame de destinos en un archivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de los destinos.
    """
    guardar_csv(df_nuevo, 'models/DB/destinos.csv')

def imprimir_destinos() -> None:
    """
    Imprime la lista de destinos en la consola.
    """
    df = obtener_destinos()
    print(df.to_string(justify="center"))

def nuevo_destino(destino: Destino) -> None:
    """
    Agrega un nuevo destino al archivo CSV.
    
    Args:
        destino (dict): Diccionario con los datos del destino a agregar.
    """
    # Verificar si el valor de cliente es correcto
    if not (type(destino["ciudad"]) == str and type(destino["pais"]) == str and type(destino["costo_base"]) == float):
        print("El destino nuevo no es correcto.")
        return
    destino["id_destino"] = destino["pais"].capitalize()[:3] + destino["ciudad"].capitalize()[:3]
    destino["disponible"] = True
    # Verificar si el destino ya existe
    if es_destino(destino["id_destino"]):
        print("El destino ya existe.")
        return
    df = obtener_destinos()
    df.loc[len(df)] = destino
    guardar_destinos(df)

def obtener_destino(id_destino: str) -> Destino| None:
    """
    Obtiene un destino específico por su id_destino.
    
    Args:
        id_destino (str): id_destino del destino a buscar.
    
    Returns:
        dict: Diccionario con los datos del destino encontrado, o None si no se encuentra.
    """
    if not es_destino(id_destino):
        print("destino no encontrado.")
        return None
    else:
        df = obtener_destinos()
        destino = df[df['id_destino'] == id_destino]
        return destino.iloc[0].to_dict()
    
def delete_destino(id_destino:str) -> None:
    """
    Elimina un destino específico por su id_destino.
    
    Args:
        id_destino (str): id_destino del destino a eliminar.
    """
    df = obtener_destinos()
    df = df[df['id_destino'] != id_destino]
    guardar_destinos(df)

def alternar_disponibilidad_destino(id_destino: str) -> None:
    """
    Cambia el estado de disponibilidad de un destino según su id_destino.
    
    Si estaba disponible, lo marca como no disponible. Si no estaba disponible, lo vuelve a activar.
    
    Args:
        id_destino (str): ID del destino a modificar.
    """
    df = obtener_destinos()

    # Verificamos si el destino existe
    if id_destino in df['id_destino'].astype(str).values:
        # Encontramos el índice del destino
        idx = df[df['id_destino'].astype(str) == id_destino].index
        # Invertimos el valor de disponible
        df.loc[idx, 'disponible'] = ~df.loc[idx, 'disponible']
        guardar_destinos(df)
        print(f"Se modificó la disponibilidad del destino {id_destino}.")
    else:
        print(f"No se encontró un destino con id_destino = {id_destino}.")

def es_destino(id_destino: str) -> bool:
    """
    Verifica si un destino existe por su id_destino.
    
    Args:
        id_destino (str): id_destino del destino a verificar.
    
    Returns:
        bool: True si el destino existe, False en caso contrario.
    """
    df = obtener_destinos()
    return not df[df['id_destino'] == id_destino].empty