"""Add password_hash to User

Revision ID: 21d35faa8dc5
Revises: 
Create Date: 2025-03-07 15:17:06.620019
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21d35faa8dc5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Ensure no NULL password_hash values exist
    op.execute("UPDATE user SET password_hash = '' WHERE password_hash IS NULL")
    
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(255), nullable=False, default=''))

def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')
