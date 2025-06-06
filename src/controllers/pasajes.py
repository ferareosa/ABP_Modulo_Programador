from datetime import datetime
from .scripts import opcion_ingresada
from .scripts import es_opcion_correcta
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
from ..types import Cliente
from ..types import Destino

def gestionar_pasajes()-> int | None:
    print("\n-- GESTIONAR PASAJES --")
    print("1. Ver Pasajes Comprados")
    print("2. Comprar Pasaje")
    print("3. Cancelar Pasaje (Boton de Arrepentimiento)")
    print("4. Volver al Menú Principal")
    print("=============================================================")
    opcion = opcion_ingresada()
    if es_opcion_correcta(opcion, 4):
        return opcion
    return None

def detalle_pasaje():
    pass

def ver_pasajes():
    imprimir_registro()
    print("=============================================================")

def elejir_cliente()-> Cliente | None:
    print("1. Nuevo Cliente")
    print("2. Seleccionar Cliente Existente")
    print("3. Volver al Anterior")
    print("=============================================================")
    opcion = opcion_ingresada()
    if es_opcion_correcta(opcion, 3):
        if opcion == 1:
            print("Opción 1 seleccionada: Nuevo Cliente")
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
            print("Opción 2 seleccionada: Seleccionar Cliente Existente")
            imprimir_clientes()
            cuit = opcion_ingresada("Ingrese el CUIT del cliente: ")
            return obtener_cliente(cuit)
        else:
            print("=============================================================")
            return None

def elejir_destino()-> Destino | None:
    imprimir_destinos()
    print("=============================================================")
    id = dato_ingresado("ID del destino", "str")
    return obtener_destino(id)

def compra_de_pasaje()-> None | int :
    print("\n-- COMPRA DE PASAJES --")
    print("\n-- Quien hace la compra? --")
    cliente = elejir_cliente()
    if not cliente:return None
    print("\n-- A que destino viaja? --")
    destino = elejir_destino()
    if not destino or not destino["disponible"]:
        print("Destino no valido.")
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
    print("\n-- CANCELACION DE PASAJES --")
    print("--(BOTON DE ARREPENTIMIENTO)--")
    print("\n-- Seleccione el pasaje a cancelar --")
    imprimir_registro()
    id_pasaje = dato_ingresado("ID del pasaje a cancelar", "int")
    if not id_pasaje:
        print("Error: ID de pasaje no válido.")
        return None
    else:
        cancelar_pasaje(id_pasaje)
        if no_continuar("¿Desea cancelar otro pasaje? (s/n)"): return None
        else: return 3
