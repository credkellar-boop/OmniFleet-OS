import logging

class SolarManager:
    def __init__(self):
        self.roof_output_watts = 0.0
        self.is_charging = False

    def track_sunlight(self, lux_level: float):
        """Calculates energy yield based on current ambient light sensors."""
        if lux_level > 50000: # Direct sunlight threshold
            self.roof_output_watts = 300.0
            self.is_charging = True
            logging.info("Direct sunlight detected. Routing 300W to HV battery.")
        elif lux_level > 10000:
            self.roof_output_watts = 50.0
            self.is_charging = True
        else:
            self.roof_output_watts = 0.0
            self.is_charging = False

        return self.roof_output_watts
      
