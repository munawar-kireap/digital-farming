from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.core.database.connectivity.sync_connect import get_sync_db
from app.core.database.tables.sample_tables import SampleTable
from app.features.sample.data.services.sample_service import SampleService
from app.features.sample.domain.req_models.sample_add_v0 import (
    SampleAddV0ReqModel,
)
from app.features.sample.domain.res_models.sample_add_v0 import (
    SampleAddV0ResModel,
)
from app.shared.config.endpoints.details import APIEndpointDetail
from app.shared.config.routers.setup import RouterSetup


sample_router_V0 = APIRouter(
    prefix=RouterSetup.sample_router_v0.prefix,
    tags=RouterSetup.sample_router_v0.tag
    )


@sample_router_V0.post(path=APIEndpointDetail.sample_add_v0.path,
                       summary=APIEndpointDetail.sample_add_v0.summary,
                       description=APIEndpointDetail.sample_add_v0.description,
                       response_model=SampleAddV0ResModel,
                       )
async def sample_add_v0(req_body: SampleAddV0ReqModel,
                        db: Session = Depends(get_sync_db)):
    sample_service = SampleService(db)
    try:
        data: SampleTable = sample_service.add_new(name=req_body.name)
        return SampleAddV0ResModel(id=data.id, name=data.name)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@sample_router_V0.get(path=APIEndpointDetail.sample_get_v0.path)
async def sample_get_v0(db: Session = Depends(get_sync_db)):
    sample_service = SampleService(db)
    try:
        return sample_service.get_all()
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@sample_router_V0.put(path=APIEndpointDetail.sample_update_v0.path)
async def sample_update_v0(id: int, name: str, db: Session = Depends(get_sync_db)):
    sample_service = SampleService(db)
    try:
        return sample_service.update(id=id, name=name)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@sample_router_V0.delete(path=APIEndpointDetail.sample_delete_v0.path)
async def sample_delete_v0(id: int, db: Session = Depends(get_sync_db)):
    sample_service = SampleService(db)
    try:
        return sample_service.delete(id=id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

