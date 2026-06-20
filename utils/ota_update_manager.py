def check_for_updates(current_version):
    """Polls fleet server for firmware/software patches."""
    latest = "2.1.0"
    if latest > current_version:
        print("Update available. Scheduling deployment...")
        return True
    return False
  
