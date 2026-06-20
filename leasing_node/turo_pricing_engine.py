# Path: leasing_node/turo_pricing_engine.py
import logging
from datetime import datetime

class TuroPricingEngine:
    def __init__(self):
        self.base_rate = 120.00
        self.weekend_multiplier = 1.25
        self.weather_multiplier = 1.15

    def calculate_dynamic_rate(self, is_high_demand_event: bool, weather_condition: str) -> float:
        """Computes the optimized rental price point per 24-hour cycle."""
        current_rate = self.base_rate
        day_of_week = datetime.now().weekday()

        # Apply weekend surge adjustments (Friday = 4, Saturday = 5, Sunday = 6)
        if day_of_week >= 4:
            current_rate *= self.weekend_multiplier

        # Adjust for adverse weather driving up platform vehicle scarcity
        if weather_condition in ["RAINY", "SNOWY", "STORMY"]:
            current_rate *= self.weather_multiplier

        # High-impact regional events (Concerts, festivals, sports events)
        if is_high_demand_event:
            current_rate *= 1.40

        optimized_rate = round(current_rate, 2)
        logging.info(f"Dynamic rate computed: ${optimized_rate}/day [Base: ${self.base_rate}]")
        return optimized_rate
