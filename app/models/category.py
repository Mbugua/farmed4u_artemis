from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy.types import ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
import uuid

import datetime


class Category(Base):
    __tablename__ = "categories"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(String(64), index=True, nullable=False, unique=True)
    tags = Column(ARRAY(String), index=True, nullable=True)
    is_published = Column(Boolean, default=False, nullable=False)
    created_by = Column(String(64), index=True, nullable=False)
    created_at = Column(DateTime, index=True, default=datetime.datetime.utcnow())
    updated_at = Column(
        DateTime,
        index=True,
        default=datetime.datetime.utcnow(),
        onupdate=datetime.datetime.utcnow(),
    )
    sub_categories = relationship("SubCategory", backref="Categories", lazy="joined")


class SubCategory(Base):
    __tablename__ = "sub_categories"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    category_id = Column(UUID, ForeignKey("categories.id"))
    name = Column(String(32), unique=True, index=True, nullable=False)
    description = Column(String(255), index=True, nullable=True)
    tags = Column(ARRAY(String), index=True, nullable=True)
