"""Create Python package entity rules

Revision ID: db6290ac490d
Revises: abb1a0a90885
Create Date: 2021-06-01 08:33:48.909928+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "db6290ac490d"
down_revision = "abb1a0a90885"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "python_package_version_entity_rule",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("package_name", sa.Text(), nullable=False),
        sa.Column("version_range", sa.Text(), nullable=True),
        sa.Column("python_package_index_id", sa.Integer(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["python_package_index_id"], ["python_package_index.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_index(
        "python_package_version_entity_rule_package_name_idx",
        "python_package_version_entity_rule",
        ["package_name"],
        unique=False,
    )
    op.create_table(
        "python_package_version_entity_rules_association",
        sa.Column("python_package_version_entity_id", sa.Integer(), nullable=False),
        sa.Column("python_package_version_entity_rule_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["python_package_version_entity_id"], ["python_package_version_entity.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["python_package_version_entity_rule_id"], ["python_package_version_entity_rule.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("python_package_version_entity_id", "python_package_version_entity_rule_id"),
    )
    op.create_index(
        "python_entity_rules_association_table_idx",
        "python_package_version_entity_rules_association",
        ["python_package_version_entity_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "python_entity_rules_association_table_idx", table_name="python_package_version_entity_rules_association"
    )
    op.drop_table("python_package_version_entity_rules_association")
    op.drop_index(
        "python_package_version_entity_rule_package_name_idx", table_name="python_package_version_entity_rule"
    )
    op.drop_table("python_package_version_entity_rule")
    # ### end Alembic commands ###
