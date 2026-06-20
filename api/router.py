from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security import APIKeyHeader

app = FastAPI(title="OmniFleet Core API Gateway")
API_KEY_HEADER = APIKeyHeader(name="X-Omni-Token")
VALID_TOKEN = "OMNI_SECURE_TOKEN_STRING_HEX_88192"

def verify_token(token: str = Depends(API_KEY_HEADER)):
    if token != VALID_TOKEN:
        raise HTTPException(status_code=403, detail="Access denied: Invalid authentication token.")
    return token

@app.get("/api/v1/fleet/status")
async def get_fleet_telemetry(token: str = Depends(verify_token)):
    """Pulls aggregated asset health logs and revenue metrics."""
    return {
        "fleet_status": "OPERATIONAL",
        "active_assets": 14,
        "global_efficiency_score": 0.94,
        "daily_yield_accumulated_usd": 1680.50
    }
  
