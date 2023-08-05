"""Remove platform from Depends On

Revision ID: 894ddaef0c43
Revises: 50081eea5da2
Create Date: 2021-06-16 07:52:16.338937+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "894ddaef0c43"
down_revision = "50081eea5da2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("depends_on_platform", table_name="depends_on")
    op.drop_column("depends_on", "platform")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "depends_on",
        sa.Column(
            "platform", sa.TEXT(), server_default=sa.text("'linux-x86_64'::text"), autoincrement=False, nullable=False
        ),
    )
    op.create_index("depends_on_platform", "depends_on", ["platform"], unique=False)
    # ### end Alembic commands ###
