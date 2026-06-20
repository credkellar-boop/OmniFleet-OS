def calculate_solar_yield(irradiance_w_m2, panel_efficiency=0.24):
    """Calculates potential wattage from rooftop PV panels."""
    # Logic for surface area and current sun exposure
    area_sq_meters = 2.5 
    return irradiance_w_m2 * area_sq_meters * panel_efficiency

def optimize_charging_profile(soc):
    """Adjusts solar charging based on State of Charge."""
    if soc > 90:
        return "TRICKLE_CHARGE"
    return "MAX_POWER_TRANSFER"
  
