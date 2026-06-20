def is_authorized_airspace(lat, lon):
    """Checks GPS coordinates against restricted no-fly zone database."""
    # Mock database of no-fly zones (e.g., airports, government buildings)
    restricted_zones = [(34.05, -118.24)] 
    
    for zone in restricted_zones:
        if abs(lat - zone[0]) < 0.01 and abs(lon - zone[1]) < 0.01:
            return False
    return True
  
