from pydantic import BaseModel
import json


class Schema(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_loads = json.loads
        json_dumps = json.dumps
        arbitrary_types_allowed = True
