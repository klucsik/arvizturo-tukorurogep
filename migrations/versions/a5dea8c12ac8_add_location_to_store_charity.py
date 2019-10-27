"""Add location to Store, Charity.

Revision ID: a5dea8c12ac8
Revises: 4ab2ff23b3eb
Create Date: 2019-10-27 02:28:20.138889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5dea8c12ac8'
down_revision = '4ab2ff23b3eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charity', sa.Column('latitude', sa.Numeric(), nullable=True))
    op.add_column('charity', sa.Column('longitude', sa.Numeric(), nullable=True))
    op.add_column('stores', sa.Column('latitude', sa.Numeric(), nullable=True))
    op.add_column('stores', sa.Column('longitude', sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stores', 'longitude')
    op.drop_column('stores', 'latitude')
    op.drop_column('charity', 'longitude')
    op.drop_column('charity', 'latitude')
    # ### end Alembic commands ###