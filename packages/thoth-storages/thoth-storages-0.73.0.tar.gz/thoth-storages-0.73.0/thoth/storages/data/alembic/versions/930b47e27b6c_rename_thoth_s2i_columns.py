"""rename thoth s2i columns

Revision ID: 930b47e27b6c
Revises: c427c501f966
Create Date: 2022-01-19 16:56:54.439445+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "930b47e27b6c"
down_revision = "c427c501f966"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("external_software_environment", "thoth_s2i_image_name", new_column_name="thoth_image_name")
    op.alter_column("external_software_environment", "thoth_s2i_image_version", new_column_name="thoth_image_version")

    op.alter_column("software_environment", "thoth_s2i_image_name", new_column_name="thoth_image_name")
    op.alter_column("software_environment", "thoth_s2i_image_version", new_column_name="thoth_image_version")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("external_software_environment", "thoth_image_name", new_column_name="thoth_s2i_image_name")
    op.alter_column("external_software_environment", "thoth_image_version", new_column_name="thoth_s2i_image_version")

    op.alter_column("software_environment", "thoth_image_name", new_column_name="thoth_s2i_image_name")
    op.alter_column("software_environment", "thoth_image_version", new_column_name="thoth_s2i_image_version")
    # ### end Alembic commands ###
