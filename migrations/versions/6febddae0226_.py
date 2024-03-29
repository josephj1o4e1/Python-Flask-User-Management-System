"""empty message

Revision ID: 6febddae0226
Revises: e745e4c4c0fb
Create Date: 2023-06-25 14:42:33.056950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6febddae0226'
down_revision = 'e745e4c4c0fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users_oauth', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['google_id'])
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.create_unique_constraint(None, ['orcid_id'])
        batch_op.create_unique_constraint(None, ['facebook_id'])
        batch_op.create_unique_constraint(None, ['github_id'])
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users_oauth', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
