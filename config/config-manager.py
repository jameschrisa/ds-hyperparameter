from pathlib import Path
import yaml
import shutil
from datetime import datetime
import logging
from .defaults import DEFAULT_CONFIG

logger = logging.getLogger(__name__)

class ConfigManager:
    """Manages loading and saving of Deepseek configurations"""
    
    def __init__(self, config_path: Path = Path("data/config.yaml")):
        self.config_path = config_path
        self.backup_dir = Path("data/backups")
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from file or create default"""
        if self.config_path.exists():
            try:
                with open(self.config_path) as f:
                    config = yaml.safe_load(f)
                logger.info("Configuration loaded from %s", self.config_path)
                return config
            except Exception as e:
                logger.error("Error loading configuration: %s", str(e))
                return DEFAULT_CONFIG.copy()
        return DEFAULT_CONFIG.copy()

    def save_config(self):
        """Save current configuration to file with backup"""
        try:
            # Create backup first
            if self.config_path.exists():
                backup_path = self.backup_dir / f"config_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"
                shutil.copy(self.config_path, backup_path)
                logger.info("Created backup at %s", backup_path)

            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
            logger.info("Configuration saved to %s", self.config_path)
        except Exception as e:
            logger.error("Error saving configuration: %s", str(e))
            raise

    def reset_to_default(self):
        """Reset configuration to default values"""
        try:
            if self.config_path.exists():
                backup_path = self.backup_dir / f"config_backup_before_reset_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"
                shutil.copy(self.config_path, backup_path)
                logger.info("Created pre-reset backup at %s", backup_path)
            
            self.config = DEFAULT_CONFIG.copy()
            self.save_config()
            logger.info("Configuration reset to defaults")
        except Exception as e:
            logger.error("Error resetting configuration: %s", str(e))
            raise
