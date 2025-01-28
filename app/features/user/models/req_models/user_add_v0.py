from pydantic import (
    BaseModel,
    Field,
    field_validator
)

class UserAddV0ReqModel(BaseModel):
    email: str = Field(..., description="Email of the user")
    phone: str = Field(..., description="Phone of the user")
    password: str = Field(..., description="Password of the user")

    @field_validator("email")
    def validate_email(cls, value):
        if not value:
            raise ValueError("Email cannot be empty")
        if not '@' in value:
            raise ValueError("Email must be valid")
        return value