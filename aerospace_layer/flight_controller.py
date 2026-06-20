def initiate_flight_mode(mode):
    modes = ["DRONE", "AIRPLANE", "JET", "HELICOPTER"]
    if mode.upper() in modes:
        return f"System calibrated for {mode}"
    return "Invalid mode"
  
