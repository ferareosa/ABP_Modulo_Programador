from .scripts import dato_ingresado
from .scripts import no_continuar
from ..models import imprimir_clientes
from ..models import nuevo_cliente
from ..models import obtener_cliente
from ..models import es_cliente
from ..models import delete_cliente
from ..models import update_cliente
from ..utils import consola_rich as consola

def gestionar_clientes()-> int | None:
    return consola.mostrar_menu("-- GESTIONAR CLIENTES --", [
        "Ver Clientes",
        "Agregar Cliente",
        "Modificar Cliente",
        "Eliminar Cliente",
        "Volver al Menú Principal"
        ])

def ver_clientes():
    imprimir_clientes()

def agregar_cliente() -> None | int:
    consola.mostrar_titulo("-- NUEVO CLIENTE --")
    cuit = dato_ingresado("CUIT", "int")
    razon_social = dato_ingresado("Razon Social", "str")
    email = dato_ingresado("E-mail", "str")
    cliente = {
        "cuit": cuit,
        "razon_social": razon_social,
        "email": email
    }
    nuevo_cliente(cliente)
    if no_continuar("¿Desea agregar otro cliente? (s/n)"): return None
    else: return 2

def modificar_cliente()-> None | int:
    consola.mostrar_titulo("-- MODIFICAR CLIENTE --")
    ver_clientes()
    cuit = dato_ingresado("el CUIT del cliente a modificar: ","int")
    cliente = obtener_cliente(cuit)
    if cliente:
        consola.info("Cliente encontrado:")
        consola.mostrar_tabla(
            titulo=f"Detalles de {cliente['razon_social']}",
            columnas=["CUIT", "Razon Social", "E-mail"],
            filas=[[cliente["cuit"], cliente["razon_social"], cliente["email"]]]
        )
        consola.advertir("Ingrese los nuevos datos del cliente (deje en blanco para no modificar):")
        cuit = cliente["cuit"]
        razon_social = dato_ingresado("Nueva Razon Social", "str")  or cliente["razon_social"]
        email = dato_ingresado("Nuevo E-mail", "str") or cliente["email"]
        cliente["cuit"] = cuit
        cliente["razon_social"] = razon_social
        cliente["email"] = email
        update_cliente(cliente)
    consola.console.print("[bold blue]=============================================================[/bold blue]")
    if no_continuar("¿Desea modificar otro cliente? (s/n)"): return None
    else: return 3

def eliminar_cliente()-> None | int:
    consola.mostrar_titulo("-- ELIMINAR CLIENTE --")
    ver_clientes()
    cuit = dato_ingresado("el CUIT del cliente a Eliminar: ","int")
    if es_cliente(cuit):
        consola.info("Cliente encontrado:")
        consola.info(f"CUIT: {cuit}")
        confirmacion = no_continuar("¿Está seguro de que desea eliminar este cliente? Se eliminaran todos los registros de pasajes (s/n)")
        if confirmacion:
            consola.error("Eliminación cancelada.")
        else:
            delete_cliente(cuit)
            consola.info("Cliente eliminado.")
    else:
        consola.advertir("Cliente no encontrado.")
    consola.console.print("[bold blue]=============================================================[/bold blue]")
    if no_continuar("¿Desea eliminar otro cliente? (s/n)"): return None
    else: return 4