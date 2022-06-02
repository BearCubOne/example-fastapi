"""add user table

Revision ID: 149202cb39a3
Revises: 73cb82a067e1
Create Date: 2022-06-02 10:32:44.331831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '149202cb39a3'
down_revision = '73cb82a067e1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')                    
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
