import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.theme import Theme
from rich.markdown import Markdown
from rich.align import Align
from rich import box

# Tema personalizado para colores y estilo
custom_theme = Theme({
    "title": "bold blue",
    "option": "bold cyan",
    "warning": "yellow",
    "error": "bold red",
    "info": "green",
})

# Consola con el tema aplicado
console = Console(theme=custom_theme)

# Mostrar advertencia
def advertir(mensaje: str):
    console.print(f"[warning]⚠️  {mensaje}[/warning]")

# Mostrar error
def error(mensaje: str):
    console.print(f"[error]❌ {mensaje}[/error]")

# Mostrar mensaje informativo
def info(mensaje: str):
    console.print(f"[info]✅ {mensaje}[/info]")

def mostrar_tabla(titulo: str, columnas: list, filas: list):
    tabla = Table(
        title=f"[bold magenta]{titulo.upper()}[/bold magenta]",
        title_style="bold white",
        header_style="bold bright_blue",
        box=box.SIMPLE_HEAD,
        show_lines=True,
        padding=(0, 1),
        border_style="cyan"
    )
    for col in columnas:
        tabla.add_column(col, style="bold white", justify="center")
    for fila in filas:
        tabla.add_row(*[str(c) for c in fila])
    console.print(tabla)
    time.sleep(1)  # Pausa para que el usuario pueda ver la tabla

# Mostrar menú con opciones numeradas y encabezado
def mostrar_menu(titulo: str, opciones: list) -> int | None:
    contenido = f"[title]{titulo.upper()}[/title]"
    panel = Panel(Align.center(contenido, vertical="middle"), style="bold white", expand=False, border_style="cyan", box=box.ROUNDED)
    console.print(panel)
    for i, opcion in enumerate(opciones, 1):
        console.print(f"[option]{i}. {opcion}[/option]")
    try:
        eleccion = IntPrompt.ask(f"\n[info] Seleccione una opción [/info]")
        return eleccion
    except Exception:
        error("Entrada inválida.")
        return None

def imprimir_md(contenido: str) -> None:
    """
    Muestra un texto en formato Markdown en la consola usando Rich.
    
    Args:
        contenido (str): Texto Markdown a mostrar.
    """
    markdown = Markdown(contenido)
    console.print(Align.left(markdown))

def mostrar_titulo(titulo: str) -> int | None:
    contenido = f"[title]{titulo.upper()}[/title]"
    panel = Panel(Align.center(contenido, vertical="middle"), style="bold white", expand=False, border_style="cyan", box=box.ROUNDED)
    console.print(panel)