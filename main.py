import yaml
from hardware_layer.telemetry_node import get_system_health
from hustle_mode.surge_price_monitor import get_current_surge_multiplier
from energy_layer.energy_sync import update_total_generation
from biometric_layer.toggle_manager import is_feature_enabled

def initialize_system():
    with open("omni_config.yaml", "r") as f:
        config = yaml.safe_load(f)
    print("--- OmniFleet-OS Initialized ---")
    return config

def run_main_loop():
    config = initialize_system()
    
    # 1. Health & Energy Check
    telemetry = get_system_health()
    energy_gain = update_total_generation(telemetry)
    
    # 2. Market Opportunity Logic
    surge = get_current_surge_multiplier("LA_90001")
    
    # 3. Decision Matrix
    if surge > 1.5 and telemetry['battery_pct'] > 20:
        print("Market Opportunity: Dispatching to Rideshare Network.")
    elif energy_gain > 500:
        print("Energy Opportunity: Engaging V2G Grid Export.")
    else:
        print("Status: Idle/Leasing Mode Active.")

if __name__ == "__main__":
    run_main_loop()
