"""Add charity-stores M:M rel.

Revision ID: 4ab2ff23b3eb
Revises: 6b01db664395
Create Date: 2019-10-27 02:04:52.647998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4ab2ff23b3eb'
down_revision = '6b01db664395'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charity_stores',
    sa.Column('charity_id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['charity_id'], ['charity.id'], ),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.PrimaryKeyConstraint('charity_id', 'store_id')
    )
    op.create_foreign_key(None, 'user', 'charity', ['charity_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_table('charity_stores')
    # ### end Alembic commands ###
