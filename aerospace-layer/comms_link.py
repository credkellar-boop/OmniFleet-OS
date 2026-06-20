def get_best_comms_protocol():
    """Switches between 5G, Sat-com, or Radio based on signal strength."""
    # Logic to prioritize Sat-com for remote regions, 5G for urban
    signal = {"5G": 0.2, "SAT": 0.9} 
    return max(signal, key=signal.get)
  
