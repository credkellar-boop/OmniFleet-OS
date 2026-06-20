def compute_safe_path(sensor_data):
    """Fuses multi-modal sensor data to calculate safe maneuver."""
    if sensor_data['obstacle_distance'] < 5.0:
        return "EMERGENCY_BRAKE"
    return "MAINTAIN_VELOCITY"
  
