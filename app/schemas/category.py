from typing import Optional, Set, List
from uuid import UUID
import abc
from pydantic import BaseModel


# shared props
class CategoryBase(BaseModel):
    title: str
    tags: Optional[Set[str]]
    is_published: bool
    created_by: str


class CategoryIn(BaseModel):
    title: str
    tags: Set[str]
    is_published: bool
    created_by: str


class CategoryOut(CategoryBase):
    id: UUID

    class Config:
        orm_mode = True


class SubCategoryBase(BaseModel):
    name: str
    description: Optional[str]
    tags: Optional[Set[str]]


class SubCategoryIn(BaseModel):
    name: str
    description: str
    tags: Set[str]
    category_id: UUID


class SubCategoryOut(SubCategoryBase):
    id: UUID

    class Config:
        orm_mode = True


class FullCategory(BaseModel):
    pass


class Category(CategoryOut):
    # sub_category: Optional[List[SubCategoryOut]]
    pass
