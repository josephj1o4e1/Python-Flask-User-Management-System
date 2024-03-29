"""empty message

Revision ID: 63ad2b39f9b4
Revises: 6febddae0226
Create Date: 2023-06-25 15:36:28.738328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ad2b39f9b4'
down_revision = '6febddae0226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=False))
        batch_op.drop_constraint('users_name_key', type_='unique')
        batch_op.create_unique_constraint(None, ['username'])

    with op.batch_alter_table('users_oauth', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=False))
        batch_op.drop_constraint('users_oauth_name_key', type_='unique')
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users_oauth', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('users_oauth_name_key', ['name'])
        batch_op.drop_column('username')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('users_name_key', ['name'])
        batch_op.drop_column('username')

    # ### end Alembic commands ###
