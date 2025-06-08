import os
import time
from src.utils import consola_rich as consola

def menu_principal()-> int | None:
    return consola.mostrar_menu(
        "=== Bienvenidos a SkyRoute – Sistema de Gestión de Pasajes ===",
        [
            "Gestionar Clientes",
            "Gestionar Destinos",
            "Gestionar Pasajes",
            "Acerca del Sistema",
            "Salir"
        ]
    )

def acerca_del_sistema():
    ruta = os.path.join(os.path.dirname(__file__), "./caratula.md")
    try:
        consola.console.print("[bold blue]=============================================================[/bold blue]")
        consola.mostrar_titulo("Tecnicatura Superior en Ciencias de Datos e Inteligencia Artificial")
        with open(ruta, encoding="utf-8") as readme:
            consola.imprimir_md(readme.read())
        consola.console.print("[bold blue]=============================================================[/bold blue]")
    except FileNotFoundError:
        consola.error("No se encontró el archivo caratula.md.")
    time.sleep(1.5)  # Pausa para que el usuario pueda leer la información