def inspect_can_packet(packet):
    """Filters malicious commands to steering/brakes."""
    if packet['origin'] != "SECURE_GATEWAY":
        return "BLOCK_COMMAND" # Prevent hack attempts
    return "ALLOW"
  
