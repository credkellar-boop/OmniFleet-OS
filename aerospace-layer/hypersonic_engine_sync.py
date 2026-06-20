def monitor_hypersonic_stress(mach_number, external_temp):
    """Monitors airframe thermal integrity at hypersonic velocities."""
    if mach_number >= 5.0:
        print("WARNING: Hypersonic regime entered. Engaging ablative cooling.")
        # Logic to adjust thrust and angle of attack for thermal management
        return "THROTTLE_ADJUST"
    return "NOMINAL"
  
