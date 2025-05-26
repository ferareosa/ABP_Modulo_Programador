def opcion_ingresada(mensaje:str="Ingrese una opción: ") -> int:
    """
    Esta función solicita al usuario que ingrese una opción y verifica si es válida.
    Si la opción es válida, la devuelve; de lo contrario, muestra un mensaje de error y vuelve a solicitar la entrada.
    """
    while True:
        try:
            opcion = int(input(mensaje))
            return opcion
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")