def set_thrust_vectors(mode, vector_coords):
    """
    Adjusts engine nozzles or rotor pitch.
    VTOL modes require complex vectoring; Jet modes require directional exhaust.
    """
    if mode in ["DRONE", "HELICOPTER"]:
        return "ENGAGE_VTOL_MATRIX"
    return "ENGAGE_LINEAR_THRUST"
  
