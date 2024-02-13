import datetime

from pydantic import field_validator

from common.schemas import Schema


class CourseSchema(Schema):
    name: str
    discount: float
    price: float
    block_content: dict
    slag: str


class PromotionSchema(Schema):
    name: str
    dt_start: datetime.datetime
    dt_end: datetime.datetime
    block_content: dict
