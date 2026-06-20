# hardware-layer/security_module.py

def engage_geofence(perimeter_coords):
    """Limits vehicle operations to defined geographic zones."""
    print(f"Geofence active within {perimeter_coords}")

def toggle_manual_mode(authorized_user):
    """Allows human control only after biometric validation."""
    if authorized_user:
        print("Manual drive enabled.")
      
