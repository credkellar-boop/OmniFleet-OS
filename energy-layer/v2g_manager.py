def sell_to_grid(battery_pct, grid_demand):
    """Exports power to the grid if demand (and profit) is high."""
    if battery_pct > 50 and grid_demand == "PEAK":
        return "INITIATE_V2G_EXPORT"
    return "STBY"
  
