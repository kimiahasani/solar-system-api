"""adds Planet model

Revision ID: 179e9ed1fb1b
Revises: 
Create Date: 2022-10-26 21:23:41.300895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '179e9ed1fb1b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
