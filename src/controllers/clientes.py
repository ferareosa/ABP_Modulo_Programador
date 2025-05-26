from .scripts import dato_ingresado
from .scripts import opcion_ingresada
from .scripts import es_opcion_correcta
from .scripts import no_continuar
from ..models import imprimir_clientes
from ..models import nuevo_cliente
from ..models import obtener_cliente
from ..models import es_cliente
from ..models import delete_cliente

def gestionar_clientes()-> int | None:
    print("\n-- GESTIONAR CLIENTES --")
    print("1. Ver Clientes")
    print("2. Agregar Cliente")
    print("3. Modificar Cliente")
    print("4. Eliminar Cliente")
    print("5. Volver al Menú Principal")
    print("=============================================================")
    opcion = opcion_ingresada()
    if es_opcion_correcta(opcion, 5):
        return opcion
    return None

def ver_clientes():
    imprimir_clientes()
    print("=============================================================")

def agregar_cliente() -> None | int:
    print("\n-- NUEVO CLIENTE --")
    cuit = dato_ingresado("CUIT", "int")
    razon_social = dato_ingresado("Razon Social", "str")
    email = dato_ingresado("E-mail", "str")
    cliente = {
        "cuit": cuit,
        "razon_social": razon_social,
        "email": email
    }
    nuevo_cliente(cliente)
    print("=============================================================")
    print("=============================================================")
    if no_continuar("¿Desea agregar otro cliente? (s/n)"): return None
    else: return 2

def modificar_cliente()-> None | int:
    print("\n-- MODIFICAR CLIENTE --")
    ver_clientes()
    cuit = opcion_ingresada("Ingrese el CUIT del cliente a modificar: ")
    cliente = obtener_cliente(cuit)
    if cliente:
        print("Cliente encontrado:")
        delete_cliente(cliente["cuit"])  # Eliminar el cliente para poder modificarlo
        print(f"CUIT: {cliente['cuit']}")
        print(f"Razon Social: {cliente['razon_social']}")
        print(f"E-mail: {cliente['email']}")
        print("Ingrese los nuevos datos del cliente (deje en blanco para no modificar):")
        cuit = dato_ingresado("Nuevo CUIT", "int") or cliente["cuit"]
        razon_social = dato_ingresado("Nueva Razon Social", "str")  or cliente["razon_social"]
        email = dato_ingresado("Nuevo E-mail", "str") or cliente["email"]
        cliente["cuit"] = cuit
        cliente["razon_social"] = razon_social
        cliente["email"] = email
        nuevo_cliente(cliente)
    print("=============================================================")
    if no_continuar("¿Desea modificar otro cliente? (s/n)"): return None
    else: return 3

def eliminar_cliente()-> None | int:
    print("\n-- ELIMINAR CLIENTE --")
    ver_clientes()
    cuit = opcion_ingresada("Ingrese el CUIT del cliente a eliminar: ")
    if es_cliente(cuit):
        print("Cliente encontrado:")
        print(f"CUIT: {cuit}")
        confirmacion = no_continuar("¿Está seguro de que desea eliminar este cliente? (s/n)")
        if confirmacion:
            print("Eliminación cancelada.")
        else:
            delete_cliente(cuit)
            print("Cliente eliminado.")
    else:
        print("Cliente no encontrado.")
    print("=============================================================")
    if no_continuar("¿Desea eliminar otro cliente? (s/n)"): return None
    else: return 4