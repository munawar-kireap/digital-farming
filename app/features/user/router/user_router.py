from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session

from app.core.database.connectivity.sync_connect import get_sync_db
from app.features.user.services.user_service import UserService
from app.features.user.models.req_models.user_add_v0 import UserAddV0ReqModel
from app.features.user.models.res_models.user_add_v0 import UserAddV0ResModel
from app.shared.config.endpoints.details import APIEndpointDetail
from app.shared.config.routers.setup import RouterSetup
from app.shared.logger.setup import app_logger


user_router_V0 = APIRouter(
        prefix=RouterSetup.user_router_v0.prefix,
        tags=RouterSetup.user_router_v0.tag
    )

@user_router_V0.get(path=APIEndpointDetail.user_get_v0.path)
async def user_get_v0(db: Session = Depends(get_sync_db)):
    try:
        user_serive = UserService(db)
        return user_serive.get_all()
    except Exception as e:
        app_logger.error(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@user_router_V0.post(path=APIEndpointDetail.user_add_v0.path)
async def user_add_v0(
    req_body: UserAddV0ReqModel,
    db: Session = Depends(get_sync_db)):
    try:
        user_service = UserService(db)
        data = req_body.model_dump()
        user = user_service.add_new(data)
        return UserAddV0ResModel(id=user.id, email=user.email, phone=user.phone)
    except Exception as e:
        app_logger.error(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@user_router_V0.delete(path=APIEndpointDetail.user_delete_v0.path)
async def user_delete_v0(id: int, db: Session = Depends(get_sync_db)):
    try:
        user_service = UserService(db)
        return user_service.delete(id=id)
    except Exception as e:
        app_logger.error(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@user_router_V0.put(path=APIEndpointDetail.user_update_v0.path)
async def user_update_v0(id: int, req_body: UserAddV0ReqModel, db: Session = Depends(get_sync_db)):
    try:
        user_service = UserService(db)
        data = req_body.model_dump()
        user = user_service.update(id=id, data=data)
        return UserAddV0ResModel(id=user.id, email=user.email, phone=user.phone)
    except Exception as e:
        app_logger.error(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")