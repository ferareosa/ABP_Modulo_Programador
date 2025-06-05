from ..types import Cliente
from .scripts import ejecutar_query


def obtener_clientes() -> list[Cliente]:
    """
    Obtiene todos los clientes desde la base de datos.

    Returns:
        list[Cliente]: Lista de diccionarios con los clientes.
    """
    query = "SELECT cuit, razon_social, email FROM Cliente"
    return ejecutar_query(query, fetch=True) or []


def guardar_cliente(cliente: Cliente) -> Cliente | None:
    """
    Inserta un nuevo cliente en la base de datos si no existe.

    Args:
        cliente (Cliente): Diccionario con los datos del cliente.

    Returns:
        Cliente | None: El cliente insertado o None si ya existía o hubo error.
    """
    if not (isinstance(cliente["cuit"], int) and isinstance(cliente["razon_social"], str) and isinstance(cliente["email"], str)):
        print("Cliente no válido.")
        return None

    if es_cliente(cliente["cuit"]):
        print("El cliente ya existe.")
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


def eliminar_cliente(cuit: int) -> None:
    """
    Elimina un cliente de la base de datos.

    Args:
        cuit (int): CUIT del cliente a eliminar.
    """
    query = "DELETE FROM clientes WHERE cuit = %s"
    ejecutar_query(query, (cuit,))


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
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(f"CUIT: {cliente['cuit']} | Razon Social: {cliente['razon_social']} | Email: {cliente['email']}")

def nuevo_cliente(cliente: Cliente) -> None:
    """
    Inserta un nuevo cliente en la base de datos si no existe previamente.

    Args:
        cliente (Cliente): Diccionario con los datos del cliente.
    """
    # Verificar si ya existe un cliente con ese cuit
    existe = ejecutar_query("SELECT * FROM Cliente WHERE cuit = %s", (cliente["cuit"],), fetch=True)
    if existe:
        print("El cliente ya existe.")
        return

    query = """
        INSERT INTO Cliente (cuit, nombre, apellido, edad)
        VALUES (%s, %s, %s, %s)
    """
    params = (
        cliente["cuit"],
        cliente["nombre"],
        cliente["apellido"],
        cliente["edad"]
    )
    ejecutar_query(query, params)
    print("Cliente agregado correctamente.")


def delete_cliente(cuit: str) -> None:
    """
    Elimina un cliente de la base de datos por su CUIT.

    Args:
        cuit (str): CUIT del cliente a eliminar.
    """
    # Verificar si el cliente existe
    existe = ejecutar_query("SELECT * FROM Cliente WHERE cuit = %s", (cuit,), fetch=True)
    if not existe:
        print("Cliente no encontrado.")
        return

    query = "DELETE FROM Cliente WHERE cuit = %s"
    ejecutar_query(query, (cuit,))
    print("Cliente eliminado correctamente.")