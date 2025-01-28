from pydantic import (
    BaseModel
)

class UserAddV0ResModel(BaseModel):
    id: int
    email: str
    phone: str