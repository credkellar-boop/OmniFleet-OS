def harvest_suspension_energy(vibration_frequency_hz, damper_velocity):
    """
    Simulates energy recovery from regenerative shock absorbers.
    Higher road roughness = Higher potential energy gain.
    """
    # Simplified efficiency model for electromagnetic regenerative dampers
    efficiency = 0.65 
    energy_watts = (vibration_frequency_hz * damper_velocity) * efficiency
    return energy_watts
  
