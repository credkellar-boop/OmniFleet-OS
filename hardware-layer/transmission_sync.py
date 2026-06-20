# transmission_sync.py

class DrivetrainController:
    def __init__(self, mode="Auto", drive_type="4WD"):
        self.mode = mode  # Manual, Auto
        self.drive_type = drive_type # 4WD, FWD, RWD

    def execute_shift(self, gear):
        if self.mode == "Manual":
            print(f"Waiting for driver input to shift to gear {gear}")
        else:
            print(f"Automatically shifting to gear {gear}")

    def engage_torque(self):
        if self.drive_type == "4WD":
            print("Distributing torque to all four wheels.")
          
