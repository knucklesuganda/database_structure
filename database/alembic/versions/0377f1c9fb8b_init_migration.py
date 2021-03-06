"""Init migration

Revision ID: 0377f1c9fb8b
Revises: 
Create Date: 2022-05-29 15:30:36.155392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0377f1c9fb8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
