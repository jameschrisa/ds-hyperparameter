from rich.console import Console
from rich.table import Table
import logging

logger = logging.getLogger(__name__)
console = Console()

def display_current_config(config):
    """Display current configuration in a pretty format"""
    try:
        for section, params in config.items():
            table = Table(title=f"[bold blue]{section.upper()} Parameters[/]")
            table.add_column("Parameter", style="cyan")
            table.add_column("Value", style="green")
            
            for param, value in params.items():
                table.add_row(param, str(value))
            
            console.print(table)
            console.print("")
    except Exception as e:
        logger.error("Error displaying configuration: %s", str(e))
        raise
