def broadcast_status():
    """Broadcasts current fleet state to local infrastructure."""
    status = {"id": "UNIT_01", "intent": "INTERSECTION_CROSSING", "priority": "high"}
    # Uses C-V2X protocol (Cellular-Vehicle-to-Everything)
    print(f"Broadcasting to road units: {status}")
  
