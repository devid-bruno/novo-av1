"""professor

Revision ID: 89e9abeeffd7
Revises: 476cc9e19d7f
Create Date: 2023-06-12 19:23:03.784771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89e9abeeffd7'
down_revision = '476cc9e19d7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professor', sa.Column('senha_hashed', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('professor', 'senha_hashed')
    # ### end Alembic commands ###
