import logging

class VoiceCommandProcessor:
    def __init__(self):
        self.wake_word = "Hey Omni"
        self.supported_actions = ["HVAC_UP", "HVAC_DOWN", "WINDOWS_DOWN", "LOCK_DOORS"]

    def process_audio_stream(self, audio_input: str) -> str:
        """Parses local audio stream for commands."""
        if self.wake_word.lower() in audio_input.lower():
            logging.info(f"Wake word detected. Processing command: {audio_input}")
            
            if "cold" in audio_input.lower():
                return "HVAC_UP"
            elif "window" in audio_input.lower():
                return "WINDOWS_DOWN"
                
        return "IDLE"
      
