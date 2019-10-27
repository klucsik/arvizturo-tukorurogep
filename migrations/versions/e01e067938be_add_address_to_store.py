"""Add address to store.

Revision ID: e01e067938be
Revises: a5dea8c12ac8
Create Date: 2019-10-27 02:41:04.264108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e01e067938be'
down_revision = 'a5dea8c12ac8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stores', sa.Column('address', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stores', 'address')
    # ### end Alembic commands ###
