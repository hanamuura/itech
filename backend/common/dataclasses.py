from dataclasses import dataclass

@dataclass
class MetaSchema:
    title: str
    description: dict
    h1_title: str


@dataclass
class TechnologySchema:
    name: str
