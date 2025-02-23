import questionary
from rich.console import Console
from rich.panel import Panel
import logging
from pathlib import Path
from .display import display_current_config
from .validators import NumberValidator

logger = logging.getLogger(__name__)
console = Console()

def edit_section_parameters(config, section):
    """Interactive editor for parameters within a section"""
    try:
        params = config[section]
        logger.info("Editing parameters for section: %s", section)
        
        for param, current_value in params.items():
            try:
                if isinstance(current_value, bool):
                    new_value = questionary.confirm(
                        f"Enable {param}?",
                        default=current_value
                    ).ask()
                elif isinstance(current_value, (int, float)):
                    new_value = questionary.text(
                        f"Enter new value for {param} (current: {current_value})",
                        validate=NumberValidator(
                            min_val=0 if param in ['batch_size', 'warmup_steps', 'num_epochs'] else None,
                            allow_float=isinstance(current_value, float)
                        ),
                        default=str(current_value)
                    ).ask()
                    new_value = float(new_value) if isinstance(current_value, float) else int(new_value)
                else:
                    new_value = questionary.text(
                        f"Enter new value for {param} (current: {current_value})",
                        default=str(current_value)
                    ).ask()
                
                if new_value != current_value:
                    logger.info("Parameter '%s' changed from %s to %s", param, current_value, new_value)
                    params[param] = new_value
                
            except Exception as e:
                logger.error("Error editing parameter '%s': %s", param, str(e))
                console.print(f"[red]Error editing {param}. Skipping...[/]")
                continue
    except Exception as e:
        logger.error("Error in edit_section_parameters: %s", str(e))
        raise

def view_logs():
    """Display recent log entries"""
    try:
        log_dir = Path("data/logs")
        if not log_dir.exists():
            console.print("[yellow]No logs found.[/]")
            return

        log_files = sorted(log_dir.glob("*.log"), key=lambda x: x.stat().st_mtime, reverse=True)
        if not log_files:
            console.print("[yellow]No log files found.[/]")
            return

        recent_log = log_files[0]
        with open(recent_log) as f:
            lines = f.readlines()[-20:]  # Get last 20 lines
            
        console.print(Panel("[bold blue]Recent Log Entries[/]"))
        for line in lines:
            console.print(line.strip())
        
        input("\nPress Enter to continue...")
    except Exception as e:
        logger.error("Error viewing logs: %s", str(e))
        console.print("[red]Error viewing logs. Please check the logs directory manually.[/]")

def main_menu(config_manager):
    """Main menu interface"""
    while True:
        try:
            console.clear()
            console.print(Panel("[bold blue]Deepseek R1 Hyperparameter Tuner[/]", 
                              subtitle="Interactive Configuration Tool"))
            
            display_current_config(config_manager.config)
            
            choice = questionary.select(
                "What would you like to do?",
                choices=[
                    "Edit Model Parameters",
                    "Edit Training Parameters",
                    "Edit Data Parameters",
                    "Save Configuration",
                    "Reset to Default Configuration",
                    "View Recent Logs",
                    "Exit"
                ]
            ).ask()
            
            logger.info("User selected: %s", choice)
            
            if choice == "Exit":
                if questionary.confirm("Save changes before exiting?").ask():
                    config_manager.save_config()
                    logger.info("Configuration saved before exit")
                break
            elif choice == "Save Configuration":
                config_manager.save_config()
                console.print("[green]Configuration saved successfully![/]")
                input("Press Enter to continue...")
            elif choice == "Reset to Default Configuration":
                if questionary.confirm("This will reset all parameters to default values. Continue?").ask():
                    config_manager.reset_to_default()
                    console.print("[yellow]Configuration reset to defaults.[/]")
                    logger.info("Configuration reset to defaults by user")
                    input("Press Enter to continue...")
            elif choice == "View Recent Logs":
                view_logs()
            else:
                section = choice.split()[1].lower()
                edit_section_parameters(config_manager.config, section)
                
        except Exception as e:
            logger.error("Error in main menu: %s", str(e))
            console.print(f"[red]An error occurred: {str(e)}[/]")
            input("Press Enter to continue...")
