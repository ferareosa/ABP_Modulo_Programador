from datetime import datetime
from datetime import timedelta
import pandas as pd
from ..types import Pasaje
from .scripts import cargar_o_crear_csv
from .scripts import guardar_csv
def obtener_pasajes()-> pd.DataFrame:
    """
    Obtiene la lista de pasajes desde un archivo CSV y la devuelve como un DataFrame de pandas.
    
    Returns:
        pd.DataFrame: DataFrame con los datos de los pasajes.
    """
    columnas = ['id_venta','cuit','id_destino','fecha_venta','estado','costo_total']
    return cargar_o_crear_csv('models/DB/pasajes.csv', columnas)

def guardar_compras(df_nuevo: pd.DataFrame) -> None:
    """
    Guarda el DataFrame de pasajes en un archivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de los pasajes.
    """
    guardar_csv(df_nuevo, 'models/DB/pasajes.csv')

def imprimir_registro() -> None:
    """
    Imprime la lista de compras de pasajes en la consola.
    """
    df = obtener_pasajes()
    print(df.to_string(justify="center"))

def comprar_pasaje(pasaje: Pasaje):
    """
    Registra la compra de un pasaje en el archivo CSV.
    
    Args:
        pasaje (Pasaje): Objeto Pasaje con los datos de la compra.
    """

    df = obtener_pasajes()
    df.loc[len(df)] = pasaje
    print("Pasaje comprado con éxito.")
    guardar_compras(df)

def nuevo_id_pasaje() -> int:
    """
    Genera un nuevo ID único para un pasaje.
    
    Returns:
        int: Nuevo ID de pasaje.
    """
    df = obtener_pasajes()
    if df.empty:
        return 1
    else:
        return df['id_venta'].max() + 1

def cancelar_pasaje(id_pasaje: int) -> None:
    """
    Cancela un pasaje dado su ID.

    Args:
        id_pasaje (int): ID del pasaje a cancelar.
    """
    df = obtener_pasajes()

    if id_pasaje not in df['id_venta'].values:
        print(f"Pasaje con ID {id_pasaje} no encontrado.")
        return
    
    # Verificar si el pasaje fue comprado hace más de 60 días
    fecha_de_compra = datetime.strptime(df[df['id_venta'] == id_pasaje]['fecha_venta'].values[0], '%d/%m/%Y')
    fecha_limite = fecha_de_compra + timedelta(days=60)
    fecha_actual = datetime.now()
    if fecha_actual > fecha_limite:
        print(f"Pasaje con ID {id_pasaje} no puede ser cancelado. Ha pasado el plazo de 60 días.")
        return
    
    # Cambiar el estado directamente en el DataFrame original
    df.loc[df['id_venta'] == id_pasaje, 'estado'] = False
    guardar_compras(df)

    print(f"Pasaje con ID {id_pasaje} cancelado con éxito.") 

