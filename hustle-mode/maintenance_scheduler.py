# hustle-mode/maintenance_scheduler.py

def check_service_required(telemetry):
    """Prevents dispatch if maintenance is overdue."""
    if telemetry['brake_pad_wear'] > 0.8:
        return True
    return False
  
