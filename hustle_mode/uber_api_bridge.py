import asyncio
import logging

class UberAPIBridge:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.is_dispatch_ready = False

    async def toggle_online_status(self, status: bool):
        """Switches the vehicle's availability on the rideshare network."""
        self.is_dispatch_ready = status
        state = "ONLINE" if status else "OFFLINE"
        logging.info(f"Vehicle dispatch status changed to: {state}")

    async def auto_accept_ride(self, min_fare: float):
        """Listens to the dispatch queue and accepts rides above the minimum fare."""
        if not self.is_dispatch_ready:
            return None

        logging.info(f"Listening for dispatch requests > ${min_fare}...")
        await asyncio.sleep(2)
        
        simulated_fare = 45.50
        if simulated_fare >= min_fare:
            logging.info(f"Ride accepted. Fare: ${simulated_fare}. Routing to passenger.")
            return {"status": "ACCEPTED", "fare": simulated_fare, "route_id": "R-1029"}
        return {"status": "REJECTED"}
      
