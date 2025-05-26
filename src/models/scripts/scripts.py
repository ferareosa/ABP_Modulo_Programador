import os
import pandas as pd

def ruta_absoluta(relativa_desde_modelo: str) -> str:
    """
    Devuelve una ruta absoluta segura desde el archivo que llama (como un modelo).
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # ruta actual (utils/)
    return os.path.abspath(os.path.join(base_dir, '..', '..', relativa_desde_modelo))  # vuelve a abp/

def cargar_o_crear_csv(ruta_relativa: str, columnas: list) -> pd.DataFrame:
    """
    Carga un CSV si existe. Si no, lo crea con los encabezados indicados.

    Args:
        ruta_relativa (str): Ruta relativa desde la raíz del proyecto.
        columnas (list): Lista de nombres de columnas.

    Returns:
        pd.DataFrame: DataFrame con los datos del CSV (vacío si recién creado).
    """
    ruta_csv = ruta_absoluta(ruta_relativa)

    if not os.path.exists(ruta_csv):
        print(f"Archivo no encontrado en '{ruta_relativa}'. Creando uno nuevo...")
        df_vacio = pd.DataFrame(columns=columnas)
        df_vacio.to_csv(ruta_csv, index=False)
        return df_vacio

    return pd.read_csv(ruta_csv)

def guardar_csv(df: pd.DataFrame, ruta_relativa: str) -> None:
    """
    Guarda un DataFrame en un archivo CSV.

    Args:
        df (pd.DataFrame): DataFrame a guardar.
        ruta_relativa (str): Ruta relativa desde la raíz del proyecto.
    """
    ruta_csv = ruta_absoluta(ruta_relativa)
    try:
        df.to_csv(ruta_csv, index=False)
        print(f"Datos guardados correctamente en '{ruta_relativa}'.")
    except Exception as e:
        print(f"Error al guardar los datos en '{ruta_relativa}': {e}")