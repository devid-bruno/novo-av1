"""remove_column_senha_professor

Revision ID: e1e709a85991
Revises: 89e9abeeffd7
Create Date: 2023-06-12 19:24:59.155269

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e1e709a85991'
down_revision = '89e9abeeffd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('professor', 'senha')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professor', sa.Column('senha', mysql.VARCHAR(length=255), nullable=False))
    # ### end Alembic commands ###
