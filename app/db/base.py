from .base_class import Base

# Import all the models, so that Base has them before being
# imported by Alembic]

from app.models.category import Category
