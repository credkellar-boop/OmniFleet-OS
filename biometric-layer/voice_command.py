from faster_whisper import WhisperModel
from biometric_layer.toggle_manager import is_feature_enabled

def listen_for_command():
    if not is_feature_enabled("voice_control"):
        return None
    
    # Local Whisper model initialization
    model = WhisperModel("small", device="cpu")
    print("Voice active: Listening for command...")
    # ... audio capture and parsing logic ...
  
