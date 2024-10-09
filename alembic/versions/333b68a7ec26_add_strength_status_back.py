"""add strength status back

Revision ID: 333b68a7ec26
Revises: ea947802760a
Create Date: 2024-10-09 16:37:31.362447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '333b68a7ec26'
down_revision: Union[str, None] = 'ea947802760a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('craft_essence_skills', sa.Column('strength_status', sa.Integer(), nullable=True))
    op.alter_column('craft_essence_skills', 'function_type',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('craft_essence_skills', 'function_type',
               existing_type=mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=255),
               nullable=False)
    op.drop_column('craft_essence_skills', 'strength_status')
    # ### end Alembic commands ###
