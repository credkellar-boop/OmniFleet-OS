def initiate_flight_mode(mode):
    """Configures the flight surface actuators and sensors."""
    modes = {
        "DRONE": {"stability": "high", "max_speed_knots": 60},
        "AIRPLANE": {"stability": "low", "max_speed_knots": 300},
        "JET": {"stability": "dynamic", "max_speed_knots": 1200},
        "HELICOPTER": {"stability": "hover-bias", "max_speed_knots": 150}
    }
    
    selected = modes.get(mode.upper())
    print(f"Systems calibrated for: {mode}. Stability: {selected['stability']}")
    return selected
  
