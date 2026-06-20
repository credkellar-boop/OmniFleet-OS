from energy_layer.solar_manager import calculate_solar_yield
from energy_layer.kinetic_harvester import harvest_suspension_energy

def update_total_generation(current_telemetry):
    solar = calculate_solar_yield(current_telemetry['sunlight'])
    kinetic = harvest_suspension_energy(current_telemetry['roughness'], current_telemetry['speed'])
    
    total_watts = solar + kinetic
    print(f"Generating {total_watts}W from passive sources.")
    return total_watts
  
