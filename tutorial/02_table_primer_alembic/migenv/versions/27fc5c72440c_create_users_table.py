"""create users table

Revision ID: 27fc5c72440c
Revises: 
Create Date: 2023-11-20 00:49:38.777221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27fc5c72440c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


USERS: str = "users"


def upgrade() -> None:
    op.create_table(
        USERS,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("full name", sa.Unicode(100)),
    )


def downgrade() -> None:
    op.drop_table(
        USERS,
    )

