from dataclasses import dataclass


@dataclass
class EmployeeSchema:
    full_name: str
    position: str
    career_summary: dict
