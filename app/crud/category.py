from sqlalchemy.orm import Session

from app import schemas
from app.models.category import Category, SubCategory

from typing import List, Any
from loguru import logger


def get(db: Session) -> Any:

    return db.query(Category).all()


def create_category(db: Session, category: schemas.CategoryIn) -> Category:
    category = Category(**category.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_full_category(db: Session):
    return (
        db.query(Category).filter(SubCategory.category_id == Category.id).one_or_none()
    )


def create_sub_cat(db: Session, sub_cat=schemas.SubCategoryIn) -> SubCategory:
    sub_cat = SubCategory(**sub_cat.dict())
    db.add(sub_cat)
    db.commit()
    db.refresh(sub_cat)
    return sub_cat
