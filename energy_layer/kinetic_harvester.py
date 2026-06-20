import logging

class KineticHarvester:
    def __init__(self):
        self.regen_level = "MODERATE" # Options: LOW, MODERATE, AGGRESSIVE

    def optimize_regen_profile(self, current_battery_pct: float, has_passengers: bool):
        """Adjusts motor resistance based on battery need and passenger comfort."""
        if current_battery_pct < 20.0 and not has_passengers:
            self.regen_level = "AGGRESSIVE"
            logging.info("Battery low. Empty cabin. Maximizing kinetic energy recovery.")
        elif has_passengers:
            self.regen_level = "LOW"
            logging.info("Passengers detected. Softening regen curve for ride comfort.")
        else:
            self.regen_level = "MODERATE"
            
        return self.regen_level
      
