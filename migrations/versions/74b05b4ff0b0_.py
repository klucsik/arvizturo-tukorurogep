"""empty message

Revision ID: 74b05b4ff0b0
Revises: 
Create Date: 2019-10-26 22:28:48.746923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74b05b4ff0b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chain',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('charity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('organisation_name', sa.String(length=200), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('contact_name', sa.String(length=100), nullable=True),
    sa.Column('contact_phone_number', sa.String(length=20), nullable=True),
    sa.Column('contact_email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('organisation_name')
    )
    op.create_index(op.f('ix_charity_contact_email'), 'charity', ['contact_email'], unique=True)
    op.create_table('connect_cart_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('handling_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=200), nullable=True),
    sa.Column('store', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('quantity_dimension', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('use_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('charity_id', sa.Integer(), nullable=True),
    sa.Column('chain_id', sa.Integer(), nullable=True),
    sa.Column('cart_is_open', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('charity_handling_categories',
    sa.Column('charity_id', sa.Integer(), nullable=False),
    sa.Column('handling_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['charity_id'], ['charity.id'], ),
    sa.ForeignKeyConstraint(['handling_id'], ['handling_category.id'], ),
    sa.PrimaryKeyConstraint('charity_id', 'handling_id')
    )
    op.create_table('charity_product_categories',
    sa.Column('charity_id', sa.Integer(), nullable=False),
    sa.Column('product_category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['charity_id'], ['charity.id'], ),
    sa.ForeignKeyConstraint(['product_category_id'], ['product_category.id'], ),
    sa.PrimaryKeyConstraint('charity_id', 'product_category_id')
    )
    op.create_table('charity_reuse_categories',
    sa.Column('charity_id', sa.Integer(), nullable=False),
    sa.Column('reuse_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['charity_id'], ['charity.id'], ),
    sa.ForeignKeyConstraint(['reuse_id'], ['use_category.id'], ),
    sa.PrimaryKeyConstraint('charity_id', 'reuse_id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_mapping',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chain_id', sa.Integer(), nullable=False),
    sa.Column('chain_product_id', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('product_category', sa.Integer(), nullable=False),
    sa.Column('handling_category', sa.Integer(), nullable=False),
    sa.Column('reuse_category', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chain_id'], ['chain.id'], ),
    sa.ForeignKeyConstraint(['handling_category'], ['handling_category.id'], ),
    sa.ForeignKeyConstraint(['product_category'], ['product_category.id'], ),
    sa.ForeignKeyConstraint(['reuse_category'], ['use_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.String(length=100), nullable=True),
    sa.Column('store_name', sa.String(length=100), nullable=True),
    sa.Column('chain_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chain_id'], ['chain.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stores_managed_by_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['stores.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'store_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stores_managed_by_user')
    op.drop_table('stores')
    op.drop_table('product_mapping')
    op.drop_table('order')
    op.drop_table('charity_reuse_categories')
    op.drop_table('charity_product_categories')
    op.drop_table('charity_handling_categories')
    op.drop_table('cart')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('use_category')
    op.drop_table('product_category')
    op.drop_table('product')
    op.drop_table('handling_category')
    op.drop_table('connect_cart_product')
    op.drop_index(op.f('ix_charity_contact_email'), table_name='charity')
    op.drop_table('charity')
    op.drop_table('chain')
    # ### end Alembic commands ###
