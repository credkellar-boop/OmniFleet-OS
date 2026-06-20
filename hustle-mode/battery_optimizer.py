def optimize_charge_cycle(battery_pct, energy_price_kwh):
    """Decides if it's better to charge now or keep driving."""
    # Logic to compare grid prices vs. ride revenue
    if energy_price_kwh < 0.15 and battery_pct < 40:
        return "CHARGE_IMMEDIATELY"
    return "CONTINUE_DISPATCH"
  
