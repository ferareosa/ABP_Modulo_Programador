import time
from src.controllers import menu_principal
from src.controllers import gestionar_clientes
from src.controllers import gestionar_destinos
from src.controllers import gestionar_pasajes
from src.controllers import acerca_del_sistema
from src.controllers import gestionar_pasajes
from src.controllers import ver_pasajes
from src.controllers import compra_de_pasaje
from src.controllers import cancelacion_de_pasaje
from src.controllers import ver_clientes
from src.controllers import agregar_cliente
from src.controllers import modificar_cliente
from src.controllers import eliminar_cliente
from src.controllers import ver_destinos
from src.controllers import agregar_destino
from src.controllers import modificar_destino
from src.controllers import cambiar_disponibilidad_destino
from src.utils import consola_rich as consola

def main ():
    opcion_menu_principal = None
    opcion_submenu = None
    while True:
        if opcion_menu_principal == None: opcion_menu_principal = menu_principal()
        match opcion_menu_principal:
            case 1:
                consola.info("Opción 1 seleccionada: Gestionar Clientes")
                if not opcion_submenu: opcion_submenu = gestionar_clientes()
                match opcion_submenu:
                    case 1:
                        consola.info("Opción 1 seleccionada: Ver Clientes")
                        ver_clientes()
                        opcion_submenu = None
                        continue
                    case 2:
                        consola.info("Opción 2 seleccionada: Agregar Cliente")
                        opcion_submenu = agregar_cliente()
                        continue
                    case 3:
                        consola.info("Opción 3 seleccionada: Modificar Cliente")
                        opcion_submenu = modificar_cliente()
                        continue
                    case 4:
                        consola.info("Opción 4 seleccionada: Eliminar Cliente")
                        opcion_submenu = eliminar_cliente()
                        continue
                    case 5:
                        opcion_menu_principal = None
                        opcion_submenu = None
                        consola.info("Volviendo al menú principal...")
                        continue
            case 2:
                consola.info("Opción 2 seleccionada: Gestionar Destinos")
                if not opcion_submenu: opcion_submenu = gestionar_destinos()
                match opcion_submenu:
                    case 1:
                        consola.info("Opción 1 seleccionada: Ver Destinos")
                        ver_destinos()
                        opcion_submenu = None
                        continue
                    case 2:
                        consola.info("Opción 2 seleccionada: Agregar Destino")
                        opcion_submenu = agregar_destino()
                        continue
                    case 3:
                        consola.info("Opción 3 seleccionada: Modificar Destino")
                        opcion_submenu = modificar_destino()
                        continue
                    case 4:
                        consola.info("Opción 3 seleccionada: Cambiar La Disponibilidad Del Destino")
                        opcion_submenu = cambiar_disponibilidad_destino()
                        continue
                    case 5:
                        opcion_menu_principal = None
                        opcion_submenu = None
                        consola.info("Volviendo al menú principal...")
                        continue
            case 3:
                consola.info("Opción 3 seleccionada: Gestionar Pasajes")
                if not opcion_submenu: opcion_submenu = gestionar_pasajes()
                match opcion_submenu:
                    case 1:
                        consola.info("Opción 1 seleccionada: Ver Pasajes Comprados")
                        ver_pasajes()
                        opcion_submenu = None
                        continue
                    case 2:
                        consola.info("Opción 2 seleccionada: Comprar Pasaje")
                        opcion_submenu = compra_de_pasaje()
                        continue
                    case 3:
                        consola.info("Opción 3 seleccionada: Cancelar Pasaje (Boton de Arrepentimiento)")
                        opcion_submenu = cancelacion_de_pasaje()
                        continue
                    case 4:
                        opcion_menu_principal = None
                        opcion_submenu = None
                        consola.info("Volviendo al menú principal...")
                        continue
            case 4:
                consola.info("Opción 4 seleccionada: Acerca del Sistema")
                acerca_del_sistema()
                opcion_menu_principal = None
                opcion_submenu = None
            case 5:
                consola.info("Opción 5 seleccionada: Salir del Sistema")
                consola.advertir("Saliendo del sistema...")
                time.sleep(1)
                consola.info("Muchas gracias por usar nuestro sistema de gestión de pasajes. Que tenga un buen día.")
                break
if __name__ == "__main__":
    main()