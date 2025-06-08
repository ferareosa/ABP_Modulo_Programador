from .scripts import dato_ingresado
from .scripts import no_continuar
from ..models import imprimir_destinos
from ..models import nuevo_destino
from ..models import obtener_destino
from ..models import es_destino
from ..models import alternar_disponibilidad_destino
from ..models import update_destino
from ..utils import consola_rich as consola

def gestionar_destinos()-> int | None:
    return consola.mostrar_menu(
        "-- GESTIONAR DESTINOS --",
        [
            "Ver Destinos",
            "Agregar Destino",
            "Modificar Destino",
            "Cambiar La Disponibilidad Del Destino",
            "Volver al Menú Principal"
        ]
    )

def ver_destinos():
    imprimir_destinos()
    consola.console.print("[bold blue]=============================================================[/bold blue]")

def agregar_destino()-> None | int:
    consola.mostrar_titulo("-- NUEVO DESTINO --")
    ciudad = dato_ingresado("Ciudad", "str")
    pais = dato_ingresado("Pais", "str")
    costo_base = dato_ingresado("Costo Base", "float")
    destino = {
        "ciudad": ciudad,
        "pais": pais,
        "costo_base": costo_base
    }
    nuevo_destino(destino)
    consola.console.print("[bold blue]=============================================================[/bold blue]")
    if no_continuar("¿Desea agregar otro destino? (s/n)"): return None
    else: return 2

def modificar_destino()-> None | int:
    consola.mostrar_titulo("-- MODIFICAR DESTINO --")
    ver_destinos()
    id = dato_ingresado("ID del destino a modificar: ", "int")
    destino = obtener_destino(id)
    if destino:
        consola.info("Destino encontrado:")
        consola.mostrar_tabla(
            titulo=f"Detalles de {destino['ciudad']}, {destino['pais']}",
            columnas=["ID", "Pais", "Ciudad", "Costo Base"],
            filas=[[destino["id_destino"], destino["pais"], destino["ciudad"], f"${destino['costo_base']}"]]
        )
        consola.advertir("Ingrese los nuevos datos del destino (deje en blanco para no modificar):")
        pais = dato_ingresado("Nuevo Pais", "str") or destino["pais"]
        ciudad = dato_ingresado("Nueva Ciudad", "str")  or destino["ciudad"]
        costo_base = dato_ingresado("Nuevo Precio", "float") or destino["costo_base"]
        destino["pais"] = pais
        destino["ciudad"] = ciudad
        destino["costo_base"] = costo_base
        if no_continuar("¿Está seguro de que desea modificar este destino? (s/n)"):
            consola.error("Modificacion cancelada.")
        else:
            update_destino(destino)
    consola.console.print("[bold blue]=============================================================[/bold blue]")
    if no_continuar("¿Desea modificar otro destino? (s/n)"): return None
    else: return 3

def cambiar_disponibilidad_destino()-> None | int:
    consola.mostrar_titulo("-- ACTIVAR/DESACTIVAR DESTINO --")
    ver_destinos()
    id = dato_ingresado("ID", "str")
    if es_destino(id):
        consola.info("Destino encontrado:")
        print(f"ID: {id}") 
        if no_continuar("¿Está seguro de que desea cambiar la disponibilidad de este destino? (s/n)"):
            consola.error("Modificacion cancelada.")
        else:
            alternar_disponibilidad_destino(id)
    else:
        consola.error("Cliente no encontrado.")
    consola.console.print("[bold blue]=============================================================[/bold blue]")
    if no_continuar("¿Desea modificar la disponibilidad de otro destino? (s/n)"):return None
    else: return 4