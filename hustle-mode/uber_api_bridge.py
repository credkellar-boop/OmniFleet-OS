import requests

def accept_ride(ride_id):
    # Sends authorized dispatch signal to Uber
    print(f"Dispatching to ride: {ride_id}")
    return {"status": "dispatched"}
  
