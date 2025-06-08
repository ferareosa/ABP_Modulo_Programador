from datetime import datetime
from .scripts import no_continuar
from .scripts import dato_ingresado
from ..models import imprimir_registro
from ..models import imprimir_destinos
from ..models import obtener_destino
from ..models import comprar_pasaje
from ..models import cancelar_pasaje
from ..models import nuevo_cliente
from ..models import obtener_cliente
from ..models import imprimir_clientes
from ..models import obtener_pasaje
from ..types import Cliente
from ..types import Destino
from ..utils import consola_rich as consola

def gestionar_pasajes()-> int | None:
    return consola.mostrar_menu(
        "-- GESTIONAR PASAJES --",
        [
            "Ver Pasajes Comprados",
            "Comprar Pasaje",
            "Cancelar Pasaje (Boton de Arrepentimiento)",
            "Volver al Menú Principal"
        ]
    )

def detalle_pasaje(id_venta):
    detalle_de_pasaje = obtener_pasaje(id_venta)
    if not detalle_de_pasaje:return
    else:
        cuit = detalle_de_pasaje['cuit']
        razon_social = detalle_de_pasaje['razon_social']
        destino = f"{detalle_de_pasaje['pais']}, {detalle_de_pasaje['ciudad']}"
        fecha = detalle_de_pasaje['fecha_venta']
        estado = '[info] Activo[/info]' if detalle_de_pasaje['estado'] else '[error] Inactivo[/error]'
        costo = detalle_de_pasaje['costo_total']
        consola.mostrar_tabla(
            titulo=f"Detalle del Pasaje ID: {id_venta}",
            columnas=["ID Venta", "CUIT", "Razon Social", "Destino", "Fecha", "Estado", "Costo"],
            filas=[[id_venta, cuit, razon_social, destino, fecha, estado, f"${costo}"]])


def ver_pasajes():
    imprimir_registro()
    consola.console.print("[bold blue]=============================================================[/bold blue]")
    if no_continuar("Desea ver el detalle de algun pasaje? (s/n):"): return
    else: detalle_pasaje(dato_ingresado("ID de la venta", "int"))

def elejir_cliente()-> Cliente | None:
    opcion= consola.mostrar_menu(
        "-- Quien hace la compra? --",
        [
            "Nuevo Cliente",
            "Seleccionar Cliente Existente",
            "Volver al Anterior"
        ]
    )
    
    if opcion == 1:
        consola.info("Opción 1 seleccionada: Nuevo Cliente")
        cuit = dato_ingresado("CUIT", "int")
        razon_social = dato_ingresado("Razon Social", "str")
        email = dato_ingresado("E-mail", "str")
        cliente = {
            "cuit": cuit,
            "razon_social": razon_social,
            "email": email
            }
        return nuevo_cliente(cliente)
    elif opcion == 2:
        consola.info("Opción 2 seleccionada: Seleccionar Cliente Existente")
        imprimir_clientes()
        cuit = dato_ingresado("CUIT del cliente: ", "int")
        return obtener_cliente(cuit)
    else:
        consola.console.print("[bold blue]=============================================================[/bold blue]")
        return None

def elejir_destino()-> Destino | None:
    consola.mostrar_titulo("-- A que destino viaja? --")
    imprimir_destinos()
    consola.console.print("[bold blue]=============================================================[/bold blue]")
    id = dato_ingresado("ID del destino", "int")
    return obtener_destino(id)

def compra_de_pasaje()-> None | int :
    consola.mostrar_titulo("-- COMPRA DE PASAJES --")
    cliente = elejir_cliente()
    if not cliente:return None
    destino = elejir_destino()
    if not destino or not destino["disponible"]:
        consola.error("Destino no valido o no disponible.")
        return None
    fecha_venta = datetime.today().strftime('%d/%m/%Y')
    pasaje = {
        "cuit": cliente["cuit"],
        "id_destino": destino["id_destino"],
        "fecha_venta": fecha_venta,
        "estado": True,
        "costo_total": destino["costo_base"]
    }
    comprar_pasaje(pasaje)
    if no_continuar("¿Desea comprar otro pasaje? (s/n)"): return None
    else: return 2

def cancelacion_de_pasaje() -> None | int:
    consola.mostrar_titulo("-- CANCELACION DE PASAJES --\n--(BOTON DE ARREPENTIMIENTO)--")
    
    consola.console.print("[title] -- Seleccione el pasaje a cancelar --[/title]")
    imprimir_registro()
    id_pasaje = dato_ingresado("ID del pasaje a cancelar", "int")
    if not id_pasaje:
        consola.error("Error: ID de pasaje no válido.")
        return None
    else:
        cancelar_pasaje(id_pasaje)
        if no_continuar("¿Desea cancelar otro pasaje? (s/n)"): return None
        else: return 3
