"""followers

Revision ID: 246cee85f16c
Revises: 0759dbbecd6a
Create Date: 2022-01-28 16:08:49.927305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246cee85f16c'
down_revision = '0759dbbecd6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###