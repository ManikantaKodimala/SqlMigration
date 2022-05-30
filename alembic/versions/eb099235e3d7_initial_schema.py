"""initial_schema

Revision ID: eb099235e3d7
Revises: 
Create Date: 2022-05-27 13:10:57.546184

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'eb099235e3d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('email_id', sa.String, unique=True)
    )


def downgrade():
    op.drop("user")
