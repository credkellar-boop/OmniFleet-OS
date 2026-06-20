def set_cabin_dimensions(legroom_inches, seat_count):
    """Configures interior CAD parameters."""
    layout = {
        "is_lwb": legroom_inches > 40,
        "seats": seat_count
    }
    return layout
  
