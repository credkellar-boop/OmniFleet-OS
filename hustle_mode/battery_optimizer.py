import logging

class BatteryOptimizer:
    def __init__(self):
        self.eco_mode_active = False

    def balance_auxiliary_load(self, battery_soc: float, distance_to_target_km: float) -> dict:
        """Mitigates accessory cell drain based on remaining distance metrics."""
        directives = {"hvac_limit": "NORMAL", "compute_frequency": "MAX", "projected_efficiency_gain": 0.0}
        
        # If distance parameters exceed total current raw charge bounds, override auxiliary loads
        if battery_soc < 15.0 or distance_to_target_km > (battery_soc * 3.8):
            self.eco_mode_active = True
            logging.warning(" powertrain distance limits constrained. Shifting auxiliary profiles to eco curves.")
            directives["hvac_limit"] = "ECO_MIN"
            directives["compute_frequency"] = "POWER_SAVER"
            directives["projected_efficiency_gain"] = 18.5
        else:
            self.eco_mode_active = False
            
        return directives
      
