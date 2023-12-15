from dataclasses import dataclass


@dataclass
class CompanySchema:
    name: str
    block_content: dict


@dataclass
class CompanyCaseSchema:
    title: str
    block_content: dict
    slag: str
    order_number: int
