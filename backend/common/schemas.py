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


class ImageSchema(Schema):
    path: str


class MetaSchema(Schema):
    title: str
    description: str
    h1_title: str


class TechnologySchema(Schema):
    name: str
