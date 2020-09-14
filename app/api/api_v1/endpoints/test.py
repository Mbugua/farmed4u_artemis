from fastapi import APIRouter, Request, Response, HTTPException, Depends

from sqlalchemy.orm import Session

from typing import Any, List, Type

from app.api.utils import dependencies
from app.schemas.category import Category, SubCategoryOut, SubCategoryIn, FullCategory
from app import crud
from loguru import logger

router = APIRouter()


@router.get("/", response_model=List[Category], tags=["cats"])
def get_categories(
    *, request: Request, db: Session = Depends(dependencies.get_db)
) -> Any:
    categories = crud.category.get(db)
    request.app.logger.info("fetching categories.... {}", categories)

    return categories


@router.post("/category", response_model=Category, tags=["cat"])
def create_category(
    *, db: Session = Depends(dependencies.get_db), category: Category
) -> List[Category]:

    category = crud.category.create_category(db, category)
    return category


@router.get("/super", tags=["full_cat"])
def get_full(*, request: Request, db: Session = Depends(dependencies.get_db)):
    _full = crud.category.get_full_category(db)

    # logger.debug("full category {}", _full)
    return _full


@router.post("/sub", response_model=SubCategoryOut, tags=["sub"])
def create_sub_Cat(
    *, db: Session = Depends(dependencies.get_db), sub_cat: SubCategoryIn
) -> Any:
    return crud.category.create_sub_cat(db, sub_cat)
