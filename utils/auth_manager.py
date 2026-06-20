# utils/auth_manager.py
import os

def get_api_key(service_name):
    """Retrieves secure credentials from env vars."""
    return os.getenv(f"{service_name.upper()}_API_KEY")
  
