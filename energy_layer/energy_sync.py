def update_total_generation(telemetry):
    # Summing solar + kinetic
    return telemetry.get('solar_wattage', 0) + telemetry.get('kinetic_wattage', 0)
  
