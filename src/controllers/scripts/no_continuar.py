def no_continuar(mensaje = "Desea continuar? (y/n): ") -> bool:
    """Pregunta al usuario si desea continuar y devuelve True si no desea continuar."""
    opcion = input(mensaje) or "y"
    return opcion[0].lower() == "n"