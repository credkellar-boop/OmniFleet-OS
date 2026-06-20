def check_profitability(ride_cost, energy_cost):
    """Calculate if the surge pricing covers the cost of electricity."""
    margin = ride_cost - energy_cost
    return margin > 5.00 # Target minimum profit per ride
