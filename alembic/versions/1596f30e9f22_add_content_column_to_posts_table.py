"""add content column to posts table

Revision ID: 1596f30e9f22
Revises: ca3b49403fe6
Create Date: 2025-08-28 09:31:20.568580

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1596f30e9f22"
down_revision: Union[str, Sequence[str], None] = "ca3b49403fe6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
