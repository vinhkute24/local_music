"""song db upload 3

Revision ID: 9fbb8d958c32
Revises: 5b373dfc6b6b
Create Date: 2022-07-18 17:27:00.587956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fbb8d958c32'
down_revision = '5b373dfc6b6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('file_src', sa.String(length=150)))
    op.drop_column('song', 'file_name')
    # ### end Alembic commands ###
    op.execute("COMMIT")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('file_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    op.drop_column('song', 'file_src')
    # ### end Alembic commands ###
    op.execute("COMMIT")
