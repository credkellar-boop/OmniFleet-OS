import random

class SurgePriceMonitor:
    def __init__(self, target_zones: list):
        self.zones = target_zones
        self.current_surges = {zone: 1.0 for zone in target_zones}

    def poll_zones(self) -> dict:
        """Simulates polling geo-bounded areas for price multipliers."""
        for zone in self.zones:
            # Simulate market volatility
            surge = round(random.uniform(1.0, 3.5), 2)
            self.current_surges[zone] = surge
            
        return self.current_surges

    def get_highest_yield_zone(self) -> str:
        """Returns the zone with the current highest multiplier."""
        self.poll_zones()
        best_zone = max(self.current_surges, key=self.current_surges.get)
        return best_zone
      
