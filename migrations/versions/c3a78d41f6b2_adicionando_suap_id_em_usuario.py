"""adiciona suap_id em Usuario

Revision ID: c3a78d41f6b2
Revises: 7b4a9c2d1e8f
"""
from alembic import op
import sqlalchemy as sa


revision = 'c3a78d41f6b2'
down_revision = '7b4a9c2d1e8f'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('suap_id', sa.String(length=64), nullable=True))
        batch_op.create_unique_constraint('uq_usuario_suap_id', ['suap_id'])


def downgrade():
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_constraint('uq_usuario_suap_id', type_='unique')
        batch_op.drop_column('suap_id')
