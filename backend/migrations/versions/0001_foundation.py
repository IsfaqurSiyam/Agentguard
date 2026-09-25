"""foundation migration marker

Revision ID: 0001_foundation
Revises:
Create Date: 2026-09-20
"""

revision = "0001_foundation"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Phase 1 intentionally creates no domain tables.
    pass


def downgrade() -> None:
    pass
