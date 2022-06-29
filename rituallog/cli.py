from typing import Optional
import typer
from rituallog.core import add_ritual_to_db, get_rituals_from_db
from rich.table import Table
from rich.console import Console

main = typer.Typer(help='AOP Rituals Management Application')

console = Console()


@main.command('add')
def add(
    name: str,
    element: str,
    circle: int,
    cost: int,
    execution: str,
    range: str,
    target: str,
    duration: str,
    mat_comp: str = typer.Option(default="?"),
    resistance: str = typer.Option(default=""),
):
    """Adds a new ritual to database"""
    if add_ritual_to_db(
        name,
        element,
        circle,
        cost,
        execution,
        range,
        target,
        duration,
        mat_comp,
        resistance,
    ):
        print('🎲 Ritual added to database 🎲')


@main.command('list')
def list_rituals(element: Optional[str] = None):
    """Lists Beer in database"""

    rituals = get_rituals_from_db()
    table = Table(title='🎲 rituallog 🎲')
    headers = [
        'id',
        'name',
        'element',
        'circle',
        'cost',
        'execution',
        'range',
        'target',
        'duration',
        'mat_comp',
        'resistance',
        'date',
    ]

    for header in headers:
        table.add_column(header, style='magenta')

    for ritual in rituals:
        ritual.date = ritual.date.strftime('%Y-%m-%d')
        values = [str(getattr(ritual, header)) for header in headers]
        table.add_row(*values)

    console.print(table)
