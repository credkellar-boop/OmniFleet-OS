# leasing-node/turo_pricing_engine.py

def calculate_dynamic_rate(base_rate, demand_factor, is_4wd_season):
    """Adjusts Turo rental rates in real-time."""
    if is_4wd_season:
        return base_rate * demand_factor * 1.25 # Premium for 4WD
    return base_rate * demand_factor
  
