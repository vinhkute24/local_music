"""update role

Revision ID: 297ae6845e53
Revises: d01579762f70
Create Date: 2022-07-08 15:18:16.900403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '297ae6845e53'
down_revision = 'd01579762f70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    # ### end Alembic commands ###
