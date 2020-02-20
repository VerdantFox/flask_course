"""first migration

Revision ID: fad2dc5de130
Revises: 
Create Date: 2018-03-29 16:00:53.896505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fad2dc5de130"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "puppies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("puppies")
    # ### end Alembic commands ###
