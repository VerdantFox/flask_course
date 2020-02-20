"""added owners

Revision ID: 8f6e7f7089ae
Revises: 877e9996b751
Create Date: 2018-03-30 12:37:57.274584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8f6e7f7089ae"
down_revision = "877e9996b751"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "owners",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=True),
        sa.Column("puppy_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["puppy_id"], ["puppies.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("owners")
    # ### end Alembic commands ###
