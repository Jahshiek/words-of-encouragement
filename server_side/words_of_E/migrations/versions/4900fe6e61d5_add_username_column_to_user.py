"""Add username column to user

Revision ID: 4900fe6e61d5
Revises: 21d35faa8dc5
Create Date: 2025-03-07 15:46:15.155269
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4900fe6e61d5'
down_revision = '21d35faa8dc5'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        # Adding the 'username' column
        batch_op.add_column(sa.Column('username', sa.String(length=80), nullable=False))
        
        # Altering password_hash to be non-nullable
        batch_op.alter_column('password_hash', existing_type=sa.String(), nullable=False)
        
        # Dropping old columns 'password' and 'user_name'
        batch_op.drop_column('password')
        batch_op.drop_column('user_name')

    # Update existing rows to set password_hash to '' where it is NULL
    op.execute("UPDATE user SET password_hash = '' WHERE password_hash IS NULL")


def downgrade():
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=False))
        batch_op.alter_column('password_hash', existing_type=sa.String(), nullable=True)
        batch_op.drop_column('username')
