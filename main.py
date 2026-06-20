# main.py
from hustle_mode.surge_price_monitor import get_current_surge_multiplier
from hardware_layer.telemetry_node import get_system_health
from hustle_mode.yield_optimizer import check_profitability

def run_fleet_cycle():
    telemetry = get_system_health()
    surge = get_current_surge_multiplier("LA_90001")
    
    if surge > 1.5 and not telemetry['battery_pct'] < 20:
        print("Conditions met: Dispatching to Rideshare Network.")
    else:
        print("Conditions not met: Idle/Leasing mode active.")

if __name__ == "__main__":
    run_fleet_cycle()
  
