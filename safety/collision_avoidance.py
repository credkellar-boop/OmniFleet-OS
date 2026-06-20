import logging

class CollisionAvoidanceSystem:
    def __init__(self):
        self.minimum_safe_distance_meters = 4.5
        self.override_active = False

    def evaluate_sensor_matrix(self, forward_radar_range: float, velocity_ms: float) -> str:
        """Assesses distance profiles against braking parameters to mitigate incoming collisions."""
        # Calculate dynamic stopping requirements based on vehicle speed
        dynamic_threshold = max(self.minimum_safe_distance_meters, velocity_ms * 1.2)

        if forward_radar_range <= dynamic_threshold:
            self.override_active = True
            logging.critical(f"Proximity alert breached: Object at {forward_radar_range}m. Velocity {velocity_ms}m/s. Triggering AEB.")
            return "EMERGENCY_BRAKE_ENGAGED"

        self.override_active = False
        return "CLEAR_PATH"
      
