import os
import pandas as pd
from ..types import Cliente
from .scripts import cargar_o_crear_csv
from .scripts import guardar_csv

def obtener_clientes() -> pd.DataFrame:
    """
    Obtiene la lista de clientes desde un archivo CSV. Si el archivo no existe, lo crea vacío con los encabezados esperados.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de los clientes.
    """
    columnas = ["cuit", "razon_social", "email"]
    return cargar_o_crear_csv('models/DB/clientes.csv', columnas)

def guardar_clientes(df_nuevo: pd.DataFrame) -> None:
    """
    Guarda el DataFrame de clientes en un archivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de los clientes.
    """
    guardar_csv(df_nuevo, 'models/DB/clientes.csv')

def imprimir_clientes() -> None:
    """
    Imprime la lista de clientes en la consola.
    """
    df = obtener_clientes()
    print(df.to_string(justify="center"))

def nuevo_cliente(cliente: Cliente) -> Cliente | None:
    """
    Agrega un nuevo cliente al archivo CSV.
    
    Args:
        cliente (dict): Diccionario con los datos del cliente a agregar.
    """
    # Verificar si el valor de cliente es correcto
    if not (type(cliente["cuit"]) == int and type(cliente["razon_social"]) == str and type(cliente["email"]) == str):
        print("El cliente nuevo no es correcto.")
        return
    # Verificar si el cliente ya existe
    if es_cliente(cliente["cuit"]):
        print("El cliente ya existe.")
        return
    df = obtener_clientes()
    df.loc[len(df)] = cliente
    guardar_clientes(df)
    return cliente

def obtener_cliente(cuit: int) -> Cliente | None:
    """
    Obtiene un cliente específico por su CUIT.
    
    Args:
        cuit (int): CUIT del cliente a buscar.
    
    Returns:
        dict: Diccionario con los datos del cliente encontrado, o None si no se encuentra.
    """
    if not es_cliente(cuit):
        print("Cliente no encontrado.")
        return None
    else:
        df = obtener_clientes()
        cliente = df[df['cuit'] == cuit]
        return cliente.iloc[0].to_dict()

def delete_cliente(cuit: int) -> None:
    """
    Elimina un cliente específico por su CUIT.
    
    Args:
        cuit (int): CUIT del cliente a eliminar.
    """
    df = obtener_clientes()
    df = df[df['cuit'] != cuit]
    guardar_clientes(df)

def es_cliente(cuit: int) -> bool:
    """
    Verifica si un cliente existe por su CUIT.
    
    Args:
        cuit (int): CUIT del cliente a verificar.
    
    Returns:
        bool: True si el cliente existe, False en caso contrario.
    """
    df = obtener_clientes()
    return not df[df['cuit'] == cuit].empty