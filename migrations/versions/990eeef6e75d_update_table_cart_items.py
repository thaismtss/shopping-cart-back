"""Update table cart_items

Revision ID: 990eeef6e75d
Revises: 5ab9d66da0dd
Create Date: 2024-04-15 20:03:22.560866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '990eeef6e75d'
down_revision = '5ab9d66da0dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_item', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
