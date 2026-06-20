def update_total_generation
    
    return telemetry.get('solar_wattage', 0) + telemetry.get('kinetic_wattage', 0)
  
import logging
import asyncio

class EnergySync:
    def __init__(self):
        self.aggregated_telemetry = {
            "solar_input_w": 0.0,
            "kinetic_regen_w": 0.0,
            "net_consumption_w": 0.0
        }

    async def synchronize_power_busses(self, solar_w: float, regen_w: float, current_load_w: float) -> dict:
        """Calculates concurrent multi-bus power distribution yields."""
        self.aggregated_telemetry["solar_input_w"] = solar_w
        self.aggregated_telemetry["kinetic_regen_w"] = regen_w
        self.aggregated_telemetry["net_consumption_w"] = current_load_w - (solar_w + regen_w)
        
        logging.info(f"Bus aggregation sync complete. Net system draw: {self.aggregated_telemetry['net_consumption_w']}W")
        await asyncio.sleep(0.05)
        return self.aggregated_telemetry
        
