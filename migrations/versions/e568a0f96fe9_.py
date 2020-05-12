"""empty message

Revision ID: e568a0f96fe9
Revises: edaa35d9e96c
Create Date: 2020-05-12 18:58:10.026740

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e568a0f96fe9'
down_revision = 'edaa35d9e96c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('Location_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'artist', 'locations', ['Location_id'], ['id'])
    op.drop_column('artist', 'city')
    op.drop_column('artist', 'state')
    op.create_unique_constraint(None, 'locations', ['city', 'state'])
    op.add_column('show', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.drop_column('show', 'date')
    op.add_column('venues', sa.Column('Location_id', sa.Integer(), nullable=False))
    op.drop_constraint('venues_Locations_fkey', 'venues', type_='foreignkey')
    op.create_foreign_key(None, 'venues', 'locations', ['Location_id'], ['id'])
    op.drop_column('venues', 'Locations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venues', sa.Column('Locations', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'venues', type_='foreignkey')
    op.create_foreign_key('venues_Locations_fkey', 'venues', 'locations', ['Locations'], ['id'])
    op.drop_column('venues', 'Location_id')
    op.add_column('show', sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('show', 'start_time')
    op.drop_constraint(None, 'locations', type_='unique')
    op.add_column('artist', sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('artist', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'artist', type_='foreignkey')
    op.drop_column('artist', 'Location_id')
    # ### end Alembic commands ###
