"""add ce

Revision ID: 9eb4b207d283
Revises: cc821ef8c5c0
Create Date: 2024-10-09 11:20:31.683678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9eb4b207d283'
down_revision: Union[str, None] = 'cc821ef8c5c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buffs',
    sa.Column('buff_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('buff_name', sa.String(length=255), nullable=True),
    sa.Column('buff_type', sa.String(length=255), nullable=True),
    sa.Column('related_target_trait', sa.String(length=255), nullable=True),
    sa.Column('related_self_trait', sa.String(length=255), nullable=True),
    sa.Column('related_individuality', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('buff_id')
    )
    op.create_index(op.f('ix_buffs_buff_name'), 'buffs', ['buff_name'], unique=False)
    op.create_index(op.f('ix_buffs_buff_type'), 'buffs', ['buff_type'], unique=False)
    op.create_index(op.f('ix_buffs_related_individuality'), 'buffs', ['related_individuality'], unique=False)
    op.create_index(op.f('ix_buffs_related_self_trait'), 'buffs', ['related_self_trait'], unique=False)
    op.create_index(op.f('ix_buffs_related_target_trait'), 'buffs', ['related_target_trait'], unique=False)
    op.create_table('craft_essence_skills',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('name_cn', sa.String(length=255), nullable=True, comment='中文名'),
    sa.Column('skill_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('function_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('function_type', sa.String(length=255), nullable=True),
    sa.Column('function_release_order', sa.Integer(), nullable=True),
    sa.Column('function_quest_traits', sa.String(length=255), nullable=True),
    sa.Column('function_target_traits', sa.String(length=255), nullable=True),
    sa.Column('strength_status', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('buff_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('buff_type', sa.String(length=255), nullable=True),
    sa.Column('buff_name', sa.String(length=255), nullable=True),
    sa.Column('buff_release_order', sa.Integer(), nullable=True),
    sa.Column('turn', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('userate', sa.Float(), nullable=True),
    sa.Column('rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'skill_id', 'function_id', 'strength_status', 'buff_id')
    )
    op.create_table('craft_essences',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('collection_no', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('name_cn', sa.String(length=255), nullable=True, comment='中文名'),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('max_atk', sa.Integer(), nullable=True),
    sa.Column('flag', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_craft_essences_collection_no'), 'craft_essences', ['collection_no'], unique=False)
    op.create_index(op.f('ix_craft_essences_cost'), 'craft_essences', ['cost'], unique=False)
    op.create_index(op.f('ix_craft_essences_flag'), 'craft_essences', ['flag'], unique=False)
    op.create_index(op.f('ix_craft_essences_max_atk'), 'craft_essences', ['max_atk'], unique=False)
    op.create_table('functions',
    sa.Column('function_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('function_type', sa.String(length=255), nullable=True),
    sa.Column('function_target_type', sa.String(length=255), nullable=True),
    sa.Column('function_target_team', sa.String(length=255), nullable=True),
    sa.Column('function_quest_vals', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('function_id')
    )
    op.create_index(op.f('ix_functions_function_target_team'), 'functions', ['function_target_team'], unique=False)
    op.create_index(op.f('ix_functions_function_target_type'), 'functions', ['function_target_type'], unique=False)
    op.create_index(op.f('ix_functions_function_type'), 'functions', ['function_type'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_functions_function_type'), table_name='functions')
    op.drop_index(op.f('ix_functions_function_target_type'), table_name='functions')
    op.drop_index(op.f('ix_functions_function_target_team'), table_name='functions')
    op.drop_table('functions')
    op.drop_index(op.f('ix_craft_essences_max_atk'), table_name='craft_essences')
    op.drop_index(op.f('ix_craft_essences_flag'), table_name='craft_essences')
    op.drop_index(op.f('ix_craft_essences_cost'), table_name='craft_essences')
    op.drop_index(op.f('ix_craft_essences_collection_no'), table_name='craft_essences')
    op.drop_table('craft_essences')
    op.drop_table('craft_essence_skills')
    op.drop_index(op.f('ix_buffs_related_target_trait'), table_name='buffs')
    op.drop_index(op.f('ix_buffs_related_self_trait'), table_name='buffs')
    op.drop_index(op.f('ix_buffs_related_individuality'), table_name='buffs')
    op.drop_index(op.f('ix_buffs_buff_type'), table_name='buffs')
    op.drop_index(op.f('ix_buffs_buff_name'), table_name='buffs')
    op.drop_table('buffs')
    # ### end Alembic commands ###
