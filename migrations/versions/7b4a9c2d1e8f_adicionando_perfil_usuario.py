"""adicionando perfil do usuario

Revision ID: 7b4a9c2d1e8f
Revises: 519ba7849c90
"""
from alembic import op
import sqlalchemy as sa


revision = '7b4a9c2d1e8f'
down_revision = '519ba7849c90'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('role', sa.String(length=16), nullable=False, server_default='PADRAO')
        )


def downgrade():
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('role')
