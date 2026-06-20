def adjust_torque(surface_type):
    """Sets drivetrain profile based on driving conditions."""
    modes = {
        "SNOW": "50/50_SPLIT",
        "HIGHWAY": "RWD_BIAS",
        "OFFROAD": "LOCKED_DIFF"
    }
    return modes.get(surface_type, "AUTO")
  
