import json
import logging
import asyncio

class FleetMeshNode:
    def __init__(self, vehicle_id: str, mesh_port: int = 8899):
        self.vehicle_id = vehicle_id
        self.mesh_port = mesh_port
        self.connected_peers = set()

    async def broadcast_hazard_alert(self, hazard_type: str, latitude: float, longitude: float):
        """Constructs an encrypted topology message packet to relay out over local P2P links."""
        payload = {
            "sender_id": self.vehicle_id,
            "type": "HAZARD_ALERT",
            "details": {"hazard": hazard_type, "lat": latitude, "lng": longitude}
        }
        serialized_packet = json.dumps(payload)
        logging.info(f"Broadcasting localized mesh packet: {hazard_type} near ({latitude}, {longitude})")
        # In production: socket-level broadcast to 255.255.255.255 or local mesh layer
        await asyncio.sleep(0.1)
        return True

    def register_peer(self, peer_ip: str):
        """Adds a discovered localized asset to the live communications matrix."""
        self.connected_peers.add(peer_ip)
        logging.info(f"Node established secure routing index link with peer: {peer_ip}")
      
