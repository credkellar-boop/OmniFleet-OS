import logging

class HMIController:
    def __init__(self):
        self.screen_brightness = 80
        self.current_theme = "MINIMAL_DARK"

    def sync_rider_preferences(self, rider_profile: dict):
        """Adjusts cabin displays, lighting, and media to the verified passenger's profile."""
        spotify_uri = rider_profile.get("media_playlist", "spotify:playlist:top50")
        cabin_temp = rider_profile.get("preferred_temp_f", 70)
        
        logging.info(f"Cabin profile synced. Setting HVAC to {cabin_temp}F and booting media matrix to {spotify_uri}.")
        return {"status": "SYNCED", "active_playlist": spotify_uri, "temp": cabin_temp}
      
