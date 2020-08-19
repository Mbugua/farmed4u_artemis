"""update category schema migration

Revision ID: 9e942d4843d2
Revises: 45e7c3fa4cc7
Create Date: 2020-07-27 22:18:18.990330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e942d4843d2'
down_revision = '45e7c3fa4cc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categories', 'created_by',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('categories', 'is_published',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('categories', 'title',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.create_index(op.f('ix_categories_created_at'), 'categories', ['created_at'], unique=False)
    op.create_unique_constraint(None, 'categories', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'categories', type_='unique')
    op.drop_index(op.f('ix_categories_created_at'), table_name='categories')
    op.alter_column('categories', 'title',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('categories', 'is_published',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('categories', 'created_by',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###
