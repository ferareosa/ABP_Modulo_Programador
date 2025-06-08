from rich.prompt import Prompt
from rich.console import Console

console = Console()

def no_continuar(mensaje: str = "¿Desea continuar? (s/n): ") -> bool:
    """
    Pregunta al usuario si desea continuar.
    Devuelve True si la respuesta empieza con 'n' o 'N', lo que indica que NO desea continuar.
    """
    try:
        opcion = Prompt.ask(f"[bold yellow]{mensaje}[/bold yellow]", default="s")
        return opcion.strip().lower().startswith("n")
    except KeyboardInterrupt:
        console.print("\n[bold yellow]⚠️ Entrada cancelada. Se asume que desea continuar.[/bold yellow]", style="warning")
        return False