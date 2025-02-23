#!/usr/bin/env python3
import typer
from rich.console import Console
from config.manager import ConfigManager
from ui.menu import main_menu
from utils.logger import setup_logger

app = typer.Typer(help="Interactive Deepseek R1 Hyperparameter Tuner")
console = Console()
logger = setup_logger()

@app.command()
def main():
    """Launch the interactive hyperparameter tuner"""
    try:
        logger.info("Starting Deepseek R1 Hyperparameter Tuner")
        config_manager = ConfigManager()
        main_menu(config_manager)
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
        console.print("\n[yellow]Exiting...[/]")
    except Exception as e:
        logger.error("Fatal error: %s", str(e))
        console.print(f"[red]A fatal error occurred: {str(e)}[/]")

if __name__ == "__main__":
    app.main()
