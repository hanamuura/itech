from pydantic import BaseModel
from datetime import datetime


class Schema(BaseModel):
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda d: d.isoformat
        }
