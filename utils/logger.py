import logging

logging.basicConfig(filename='fleet.log', level=logging.INFO)

def log_event(message):
    logging.info(f"FLEET_EVENT: {message}")
  
