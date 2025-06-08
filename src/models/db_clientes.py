from ..types import Cliente
from .scripts import ejecutar_query
from ..utils import consola_rich as consola

def obtener_clientes() -> list[Cliente]:
    """
    Obtiene todos los clientes desde la base de datos.

    Returns:
        list[Cliente]: Lista de diccionarios con los clientes.
    """
    query = "SELECT cuit, razon_social, email FROM Cliente"
    return ejecutar_query(query, fetch=True) or []

def nuevo_cliente(cliente: Cliente) -> Cliente | None:
    """
    Inserta un nuevo cliente en la base de datos si no existe.

    Args:
        cliente (Cliente): Diccionario con los datos del cliente.

    Returns:
        Cliente | None: El cliente insertado o None si ya existía o hubo error.
    """
    if not (isinstance(cliente["cuit"], int) and isinstance(cliente["razon_social"], str) and isinstance(cliente["email"], str)):
        consola.error("Cliente no válido.")
        return None

    if es_cliente(cliente["cuit"]):
        consola.advertir("El cliente ya existe.")
        return None

    query = """
        INSERT INTO Cliente (cuit, razon_social, email)
        VALUES (%s, %s, %s)
    """
    params = (cliente["cuit"], cliente["razon_social"], cliente["email"])
    ejecutar_query(query, params)
    return cliente

def obtener_cliente(cuit: int) -> Cliente | None:
    """
    Obtiene un cliente por su CUIT.

    Args:
        cuit (int): CUIT del cliente.

    Returns:
        Cliente | None: Diccionario con el cliente o None si no se encuentra.
    """
    query = "SELECT * FROM Cliente WHERE cuit = %s"
    resultado = ejecutar_query(query, (cuit,), fetch=True)
    return resultado[0] if resultado else None

def es_cliente(cuit: int) -> bool:
    """
    Verifica si un cliente con ese CUIT existe en la base de datos.

    Args:
        cuit (int): CUIT a verificar.

    Returns:
        bool: True si el cliente existe, False si no.
    """
    query = "SELECT 1 FROM Cliente WHERE cuit = %s"
    resultado = ejecutar_query(query, (cuit,), fetch=True)
    return bool(resultado)

def imprimir_clientes() -> None:
    """
    Imprime todos los clientes en consola.
    """
    clientes = obtener_clientes()
    if not clientes:
        consola.error("No hay clientes registrados.")
        return
    consola.mostrar_tabla(
        titulo="Clientes Registrados",
        columnas=["CUIT", "Razon Social", "Email"],
        filas=[[cliente["cuit"], cliente["razon_social"], cliente["email"]] for cliente in clientes]
        )

def delete_cliente(cuit: str) -> None:
    """
    Elimina un cliente de la base de datos por su CUIT.

    Args:
        cuit (int): CUIT del cliente a eliminar.
    """
    # Verificar si el cliente existe
    existe = ejecutar_query("SELECT * FROM Cliente WHERE cuit = %s", (cuit,), fetch=True)
    if not existe:
        consola.error("Cliente no encontrado.")
        return
    query = "DELETE FROM Cliente WHERE cuit = %s"
    ejecutar_query(query, (cuit,))
    consola.info("Cliente eliminado correctamente.")

def update_cliente(cliente:Cliente)-> None:
    """
    Modifica un cliente de la base de datos por su CUIT.

    Args:
        cuit (int): CUIT del cliente a eliminar.
    """
    existe = es_cliente(cliente["cuit"])
    if existe:
        query = '''
        UPDATE Cliente 
        SET razon_social= %s, email= %s
        WHERE cuit= %s
        '''
        ejecutar_query(query, (cliente["razon_social"], cliente["email"], cliente["cuit"]))
    else:
        nuevo_cliente(cliente)

