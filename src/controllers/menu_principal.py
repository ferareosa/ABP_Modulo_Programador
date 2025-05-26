from .scripts import opcion_ingresada
from .scripts import es_opcion_correcta

def menu_principal()-> int | None:
    print("\n=== Bienvenidos a SkyRoute – Sistema de Gestión de Pasajes ===")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Pasajes")
    print("4. Acerca del Sistema")
    print("5. Salir")
    print("=============================================================")
    opcion = opcion_ingresada()
    if es_opcion_correcta(opcion, 5):
        return opcion
    return None

def acerca_del_sistema():
    print("\n=== Acerca del Sistema ===")
    print("Este sistema permite gestionar pasajes de SkyRoute como parte de un proyecto educativo.")
    print("Desarrollado por:")
    print("Areosa, Fernando. 36131545")
    print("Muñoz Brizuela, Fátima Belén. 39824821")
    print("Varela, Mario. 31401019")
    print("Annone, Ariel Gastón. 29449852")
    print("Krenz, Catalina. 35964865")
    print("")
    print("Versión 1.0")
    print("=============================================================")