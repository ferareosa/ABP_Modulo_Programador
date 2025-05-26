def es_opcion_correcta(opcion: int, numero_opciones: int) -> bool:
    """
    Verifica si la opción ingresada por el usuario es válida.
    
    :param opcion: Opción ingresada por el usuario.
    :param numero_opciones: Número total de opciones disponibles.
    :return: True si la opción es válida, False en caso contrario.
    """
    if 1 <= opcion <= numero_opciones:
        return True
    else:
        print(f"Error: La opción {opcion} no es válida. Debe estar entre 1 y {numero_opciones}.")
        return False