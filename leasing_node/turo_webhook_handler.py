import logging
import smartcar
from fastapi import FastAPI, Request

app = FastAPI()

[span_1](start_span)class VehicleControl:
    def __init__(self, access_token: str, vehicle_id: str):
        # Create a new vehicle instance using the vehicle's unique ID and access token[span_1](end_span)
        self.vehicle = smartcar.Vehicle(vehicle_id, access_token)

    [span_2](start_span)def unlock_doors(self):
        """Unlocks the vehicle using Smartcar's API."""
        try:
            # Issue the unlock command to the vehicle remotely[span_2](end_span)
            self.vehicle.unlock()
            logging.info("Smartcar API: Vehicle unlocked successfully.")
            return True
        except smartcar.SmartcarException as e:
            logging.error(f"Smartcar API Error: {e}")
            return False

@app.post("/webhooks/turo")
async def handle_turo_event(request: Request):
    """Listens for Turo webhook payloads indicating a trip has started."""
    payload = await request.json()
    event_type = payload.get("event")
    reservation_id = payload.get("reservation_id")
    
    if event_type == "trip_started":
        logging.info(f"Turo trip {reservation_id} started. Triggering remote unlock.")
        
        # Assume token and vehicle_id are fetched from secure storage
        controller = VehicleControl(access_token="valid_oauth_token", vehicle_id="uuid-of-vehicle")
        success = controller.unlock_doors()
        
        if success:
            return {"status": "success", "message": "Vehicle unlocked"}
        else:
            return {"status": "error", "message": "Failed to unlock vehicle"}, 500
            
    return {"status": "ignored"}
  
