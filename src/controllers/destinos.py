from .scripts import dato_ingresado
from .scripts import opcion_ingresada
from .scripts import es_opcion_correcta
from .scripts import no_continuar
from ..models import imprimir_destinos
from ..models import nuevo_destino
from ..models import obtener_destino
from ..models import es_destino
from ..models import alternar_disponibilidad_destino
from ..models import delete_destino

def gestionar_destinos()-> int | None:
    print("\n-- GESTIONAR DESTINOS --")
    print("1. Ver Destinos")
    print("2. Agregar Destino")
    print("3. Modificar Destino")
    print("4. Cambiar La Disponibilidad Del Destino")
    print("5. Volver al Menú Principal")
    print("=============================================================")
    opcion = opcion_ingresada()
    if es_opcion_correcta(opcion, 5):
        return opcion
    return None

def ver_destinos():
    imprimir_destinos()
    print("=============================================================")

def agregar_destino()-> None | int:
    print("\n-- NUEVO DESTINO --")
    ciudad = dato_ingresado("Ciudad", "str")
    pais = dato_ingresado("Pais", "str")
    costo_base = dato_ingresado("Costo Base", "float")
    destino = {
        "ciudad": ciudad,
        "pais": pais,
        "costo_base": costo_base
    }
    nuevo_destino(destino)
    print("=============================================================")
    if no_continuar("¿Desea agregar otro destino? (s/n)"): return None
    else: return 2

def modificar_destino()-> None | int:
    print("\n-- MODIFICAR DESTINO --")
    ver_destinos()
    id = dato_ingresado("ID del destino a modificar: ", "str")
    destino = obtener_destino(id)
    print(destino)
    if destino:
        print("Destino encontrado:")
        print(f"ID: {destino['id_destino']}")
        print(f"Pais: {destino['pais']}")
        print(f"Ciudad: {destino['ciudad']}")
        print(f"Costo Base: {destino['costo_base']}")
        print("Ingrese los nuevos datos del destino (deje en blanco para no modificar):")
        pais = dato_ingresado("Nuevo Pais", "str") or destino["pais"]
        ciudad = dato_ingresado("Nueva Ciudad", "str")  or destino["ciudad"]
        costo_base = dato_ingresado("Nuevo Precio", "float") or destino["costo_base"]
        destino["pais"] = pais
        destino["ciudad"] = ciudad
        destino["costo_base"] = costo_base
        if no_continuar("¿Está seguro de que desea modificar este destino? (s/n)"):
            print("Modificacion cancelada.")
        else:
            print(destino)
            delete_destino(destino["id_destino"])
            nuevo_destino(destino)
    print("=============================================================")
    if no_continuar("¿Desea modificar otro destino? (s/n)"): return None
    else: return 3

def cambiar_disponibilidad_destino()-> None | int:
    print("\n-- ACTIVAR/DESACTIVAR DESTINO --")
    ver_destinos()
    id = dato_ingresado("ID", "str")
    if es_destino(id):
        print("Destino encontrado:")
        print(f"ID: {id}") 
        if no_continuar("¿Está seguro de que desea cambiar la disponibilidad de este destino? (s/n)"):
            print("Modificacion cancelada.")
        else:
            alternar_disponibilidad_destino(id)
    else:
        print("Cliente no encontrado.")
    print("=============================================================")
    if no_continuar("¿Desea modificar la disponibilidad de otro destino? (s/n)"):return None
    else: return 4