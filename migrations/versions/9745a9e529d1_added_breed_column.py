"""added breed column

Revision ID: 9745a9e529d1
Revises: 
Create Date: 2020-09-30 01:05:04.105501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9745a9e529d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###
