def order_delivery(restaurant_id, platform="DOORDASH"):
    """
    Standardized interface for food platforms.
    """
    # This logic maps to the unified delivery API (e.g., KitchenHub/Deliverect)
    print(f"Submitting order to {platform} for restaurant {restaurant_id}")
    return {"order_id": "99823", "status": "pending"}
  
