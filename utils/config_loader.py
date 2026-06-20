import yaml
import os
import logging

class ConfigLoader:
    def __init__(self, config_path: str = "omni_config.yaml"):
        self.config_path = config_path
        self.config_data = {}

    def load_and_validate(self) -> dict:
        """Parses yaml config files, validating core structural nodes."""
        if not os.path.exists(self.config_path):
            logging.error(f"Configuration initialization file not found at: {self.config_path}")
            return {}

        try:
            with open(self.config_path, "r") as file:
                self.config_data = yaml.safe_load(file) or {}
            
            # Verify explicit dependencies are defined
            if "hustle_mode" not in self.config_data or "energy_layer" not in self.config_data:
                logging.warning("Configuration layout is incomplete: Core parameters missing.")
            
            return self.config_data
        except yaml.YAMLError as e:
            logging.error(f"Failed to cleanly parse configuration text layout arrays: {e}")
            return {}
          
