import logging

class DroneUplink:
    def __init__(self):
        self.uav_docked = True

    def deploy_companion_drone(self, scan_radius_meters: int):
        """Releases a roof-mounted quadcopter to map hazardous terrain."""
        if self.uav_docked:
            logging.info(f"Releasing aerospace companion UAV. Mapping terrain within {scan_radius_meters}m radius.")
            self.uav_docked = False
            return "UAV_DEPLOYED"
            
        logging.warning("Deployment failed: UAV is already airborne or offline.")
        return "UAV_ALREADY_AIRBORNE"
      
