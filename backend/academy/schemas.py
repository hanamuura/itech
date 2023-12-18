import datetime

from common.schemas import Schema


class CourseSchema(Schema):
    name: str
    discount: float
    price: float
    block_content: dict


class PromotionSchema(Schema):
    name: str
    dt_start: datetime
    dt_end: datetime
    block_content: dict
