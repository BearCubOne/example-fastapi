"""add phonenumber

Revision ID: 169f110b2e7e
Revises: 1507adced1b7
Create Date: 2022-06-02 11:58:24.637320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '169f110b2e7e'
down_revision = '1507adced1b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
