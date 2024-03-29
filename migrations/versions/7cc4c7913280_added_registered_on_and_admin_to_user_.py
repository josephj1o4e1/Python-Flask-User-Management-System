"""added registered_on and admin to User, also added create_admin to cli in manage.py

Revision ID: 7cc4c7913280
Revises: 7f546be6f342
Create Date: 2023-06-09 20:49:25.708873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cc4c7913280'
down_revision = '7f546be6f342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('registered_on', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('admin', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('admin')
        batch_op.drop_column('registered_on')

    # ### end Alembic commands ###
