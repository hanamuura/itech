from common.schemas import Schema


class EmployeeSchema(Schema):
    full_name: str
    position: str
    career_summary: dict
