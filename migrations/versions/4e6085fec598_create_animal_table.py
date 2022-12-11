"""Create animal table

Revision ID: 4e6085fec598
Revises: 
Create Date: 2022-12-08 16:03:43.124853

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4e6085fec598"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "animal",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "phylum",
            sa.Enum(
                "MOLLUSCA",
                "PORIFERA",
                "CNIDARIA",
                "PLATYHELMINTHES",
                "NEMATODA",
                "ANNELIDA",
                "ARTHROPODA",
                "ECHINODERMATA",
                "CHORDATA",
                name="phylumchoices",
            ),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("animal")
    # ### end Alembic commands ###
