"""empty message

Revision ID: d22676900c1c
Revises: 63ad2b39f9b4
Create Date: 2023-07-24 03:41:53.466674

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd22676900c1c'
down_revision = '63ad2b39f9b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_oauth')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('google_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('facebook_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('github_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('orcid_id', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('profile_pic', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['google_id'])
        batch_op.create_unique_constraint(None, ['facebook_id'])
        batch_op.create_unique_constraint(None, ['github_id'])
        batch_op.create_unique_constraint(None, ['orcid_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('profile_pic')
        batch_op.drop_column('orcid_id')
        batch_op.drop_column('github_id')
        batch_op.drop_column('facebook_id')
        batch_op.drop_column('google_id')

    op.create_table('users_oauth',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('google_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('facebook_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('github_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('orcid_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('profile_pic', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('registered_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_confirmed', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('confirmed_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_oauth_pkey'),
    sa.UniqueConstraint('email', name='users_oauth_email_key'),
    sa.UniqueConstraint('facebook_id', name='users_oauth_facebook_id_key'),
    sa.UniqueConstraint('github_id', name='users_oauth_github_id_key'),
    sa.UniqueConstraint('google_id', name='users_oauth_google_id_key'),
    sa.UniqueConstraint('orcid_id', name='users_oauth_orcid_id_key'),
    sa.UniqueConstraint('username', name='users_oauth_username_key')
    )
    # ### end Alembic commands ###
