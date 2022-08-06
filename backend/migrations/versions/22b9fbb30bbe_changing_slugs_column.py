"""changing slugs column

Revision ID: 22b9fbb30bbe
Revises: e38b893d154f
Create Date: 2022-08-06 17:08:00.170281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22b9fbb30bbe'
down_revision = 'e38b893d154f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('slugs', sa.String(), nullable=True))
    op.drop_column('posts', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('slug', sa.VARCHAR(), nullable=True))
    op.drop_column('posts', 'slugs')
    # ### end Alembic commands ###