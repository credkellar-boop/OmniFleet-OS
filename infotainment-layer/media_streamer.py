def stream_content(service_name, content_id):
    """
    Unified trigger for media services (Netflix, Spotify, etc.)
    """
    # Logic to route to the correct platform API
    platforms = ["NETFLIX", "SPOTIFY", "YOUTUBE"]
    if service_name.upper() in platforms:
        print(f"Launching {service_name} stream for: {content_id}")
        return True
    return False
  
