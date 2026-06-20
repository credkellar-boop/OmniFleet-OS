import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class FleetStatus:
    active_nodes: int
    system_health_pct: float
    total_yield_usd: float

@strawberry.type
class Query:
    @strawberry.field
    def get_fleet_telemetry(self) -> FleetStatus:
        # Resolves high-level metrics for DevFleetSync and other dashboard engines
        return FleetStatus(active_nodes=14, system_health_pct=98.5, total_yield_usd=1680.50)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
