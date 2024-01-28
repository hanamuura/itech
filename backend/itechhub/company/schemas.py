from common.schemas import Schema


class CompanyCaseSchema(Schema):
    title: str
    block_content: str
    order_number: int


class CompanyServiceSchema(Schema):
    name: str
    order_number: int
    block_content: dict
