"""'Init'

Revision ID: 2310e9620fd8
Revises: 
Create Date: 2022-12-29 19:11:07.123844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2310e9620fd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('adresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('adress_name', sa.String(length=250), nullable=True),
    sa.Column('rec_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rec_id'], ['records.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_name', sa.String(length=100), nullable=True),
    sa.Column('rec_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rec_id'], ['records.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_name', sa.String(length=20), nullable=True),
    sa.Column('rec_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rec_id'], ['records.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('phones')
    op.drop_table('emails')
    op.drop_table('adresses')
    op.drop_table('records')
    # ### end Alembic commands ###
