# Repository: OmniFleet-OS
# Author: Credkellar-boop
# Path: main.py

import asyncio
import logging
from hustle_mode.yield_optimizer import YieldOptimizer
from energy_layer.v2g_manager import V2GManager
from leasing_node.turo_smartcar_bridge import TuroSmartcarBridge

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OmniFleetOS:
    def __init__(self):
        self.yield_optimizer = YieldOptimizer()
        self.v2g_manager = V2GManager()
        self.turo_bridge = TuroSmartcarBridge()
        self.fleet_active = True

    async def fleet_loop(self):
        logging.info("OmniFleet-OS Initialized. Scanning for yield opportunities...")
        while self.fleet_active:
            # 1. Check if it's more profitable to sell power back to the grid or drive
            grid_price = await self.v2g_manager.check_spot_pricing()
            
            # 2. Analyze Turo rentals vs Uber Autonomous Dispatch surge pricing
            best_action = await self.yield_optimizer.calculate_best_margin(grid_price)
            
            if best_action == "V2G_DISCHARGE":
                await self.v2g_manager.initiate_discharge()
            elif best_action == "TURO_HANDOFF":
                await self.turo_bridge.sync_upcoming_reservations()
            elif best_action == "UBER_DISPATCH":
                logging.info("Deploying fleet to high-surge zones.")
            
            await asyncio.sleep(60) # Re-evaluate every minute

if __name__ == "__main__":
    os_instance = OmniFleetOS()
    asyncio.run(os_instance.fleet_loop())
