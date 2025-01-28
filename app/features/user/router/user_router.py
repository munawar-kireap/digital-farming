from fastapi import (
    APIRouter
)


from app.shared.config.endpoints.details import APIEndpointDetail
from app.shared.config.routers.setup import RouterSetup


user_router_V0 = APIRouter(
        prefix=RouterSetup.user_router_v0.prefix,
        tags=RouterSetup.user_router_v0.tag
    )


