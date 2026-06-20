import datetime

def record_incident(event_type, payload):
    """Logs system state for forensic/insurance audit."""
    timestamp = datetime.datetime.now().isoformat()
    with open("flight_blackbox.log", "a") as f:
        f.write(f"[{timestamp}] {event_type}: {payload}\n")
      
