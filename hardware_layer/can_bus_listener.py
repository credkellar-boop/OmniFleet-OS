import struct
import logging

class CANBusListener:
    def __init__(self, interface: str = "can0"):
        self.interface = interface
        self.is_listening = False

    def decode_can_frame(self, can_id: int, data: bytes) -> dict:
        """Unpacks standardized raw frame hex payloads into human-readable metrics."""
        # Frame mappings: 0x101 = Battery Temp/Voltage, 0x202 = RPM/Odometer
        if can_id == 0x101:
            temp, voltage = struct.unpack("!ff", data)
            return {"metric": "battery_telemetry", "temp_c": temp, "voltage_v": voltage}
        elif can_id == 0x202:
            rpm, speed = struct.unpack("!ii", data)
            return {"metric": "drive_telemetry", "rpm": rpm, "speed_kmh": speed}
        
        return {"metric": "unknown", "raw_id": hex(can_id)}

    def process_mock_stream(self, mock_bytes: bytes) -> dict:
        """Fallback emulator processor for multi-architecture simulation testing."""
        if len(mock_bytes) < 12:
            return {"error": "Malformed frame buffer payload"}
        can_id = struct.unpack("!I", mock_bytes[:4])[0]
        data_payload = mock_bytes[4:12]
        return self.decode_can_frame(can_id, data_payload)
      
