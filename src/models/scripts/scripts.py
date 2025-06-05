import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from pathlib import Path
import os


def conectar_db():
    """
    Establece una conexión con la base de datos MySQL utilizando las variables de entorno.

    Returns:
        mysql.connector.connection_cext.CMySQLConnection | None: Objeto de conexión o None si falla.
    """
    # Cargar variables de entorno desde .env
    env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def ejecutar_query(query: str, params: tuple = None, fetch: bool = False) -> list[dict] | None:
    """
    Ejecuta una consulta SQL en la base de datos.

    Args:
        query (str): Consulta SQL.
        params (tuple, optional): Parámetros para la query (opcional).
        fetch (bool, optional): Si es True, devuelve los resultados como lista de diccionarios.

    Returns:
        list[dict] | None: Resultados si `fetch=True`. None si no se usa fetch o si hay error.
    """
    conexion = conectar_db()
    if conexion is None:
        return [] if fetch else None

    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(query, params or ())

        if fetch:
            return cursor.fetchall()

        conexion.commit()
        return None

    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return [] if fetch else None

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
