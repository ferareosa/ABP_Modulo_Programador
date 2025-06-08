from typing import Literal
from typing import Literal
from rich.prompt import Prompt, IntPrompt
from rich.console import Console

console = Console()

def dato_ingresado(nombre_dato: str, tipo: Literal["str", "int", "float"]) -> str | int | float | None:
    """
    Solicita al usuario que ingrese un valor y lo convierte al tipo especificado.
    Devuelve None si el valor ingresado no es válido.
    """

    try:
        if tipo == "str":
            dato = Prompt.ask(f"[bold cyan]Ingresar {nombre_dato}[/bold cyan]").strip()
            return dato if dato else None

        elif tipo == "int":
            return IntPrompt.ask(f"[bold cyan]Ingresar {nombre_dato}[/bold cyan]")

        elif tipo == "float":
            dato = Prompt.ask(f"[bold cyan]Ingresar {nombre_dato}[/bold cyan]")
            return float(dato)

    except ValueError:
        console.print(f"[bold red]❌ Error:[/bold red] El valor ingresado no es un {tipo}.", style="error")
        return None
    except KeyboardInterrupt:
        console.print(f"\n[bold yellow]⚠️ Entrada cancelada.[/bold yellow]", style="warning")
        return None

    return None