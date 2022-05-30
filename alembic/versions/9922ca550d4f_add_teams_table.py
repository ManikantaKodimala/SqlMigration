"""add teams table

Revision ID: 9922ca550d4f
Revises: eb099235e3d7
Create Date: 2022-05-30 10:47:18.927842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9922ca550d4f'
down_revision = 'eb099235e3d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teams')
    # ### end Alembic commands ###