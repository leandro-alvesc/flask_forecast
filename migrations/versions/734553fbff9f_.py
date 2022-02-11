"""empty message

Revision ID: 734553fbff9f
Revises: 75024df2be0d
Create Date: 2022-02-11 14:19:50.488081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '734553fbff9f'
down_revision = '75024df2be0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forecast', sa.Column('id_city', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('forecast', 'id_city')
    # ### end Alembic commands ###