"""new user reg fields

Revision ID: f77a5b54500f
Revises: 392bed2a4279
Create Date: 2024-10-10 16:17:55.783527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision: str = 'f77a5b54500f'
down_revision: Union[str, None] = '392bed2a4279'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(), nullable=False, server_default=text("'Владимир Владимирович Путян'")))
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=False, server_default=text("0")))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###
