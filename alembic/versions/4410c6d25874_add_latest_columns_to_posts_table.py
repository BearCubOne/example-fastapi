"""add latest columns to posts table

Revision ID: 4410c6d25874
Revises: d6e90fe28cae
Create Date: 2022-06-02 11:38:26.069276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4410c6d25874'
down_revision = 'd6e90fe28cae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
