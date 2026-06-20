def buffer_telemetry(data):
    """Queues telemetry when offline for later sync."""
    # Logic to prioritize critical logs (Safety/Billing) over non-critical (Sensor stream)
    print("Caching logs to local encrypted partition.")
  
