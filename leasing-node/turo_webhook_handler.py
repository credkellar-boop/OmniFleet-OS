# leasing-node/turo_webhook_handler.py

def handle_booking_event(event_payload):
    """Processes Turo booking webhooks."""
    renter = event_payload.get("renter_name")
    dates = event_payload.get("dates")
    print(f"New booking confirmed for {renter} from {dates}")
    # Logic to lock car to 'LEASING' mode here
  
