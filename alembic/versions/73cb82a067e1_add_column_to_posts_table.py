"""add column to posts table

Revision ID: 73cb82a067e1
Revises: 1173ae54abc6
Create Date: 2022-06-02 10:24:01.128211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73cb82a067e1'
down_revision = '1173ae54abc6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
