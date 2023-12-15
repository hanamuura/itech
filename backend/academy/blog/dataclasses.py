from dataclasses import dataclass


@dataclass
class BlogPostSchema:
    name: str
    block_content: dict
    slug: str


@dataclass
class BlogCategorySchema:
    name: str
    block_content: dict
    slug: str
