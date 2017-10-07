"""clean up carpool model

Revision ID: bf094584dd3c
Revises: bb34f3d9a8f4
Create Date: 2017-10-07 14:50:31.118971

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2


# revision identifiers, used by Alembic.
revision = 'bf094584dd3c'
down_revision = 'bb34f3d9a8f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpools', sa.Column('notes', sa.Text(), nullable=True))
    op.add_column('carpools', sa.Column('vehicle_description', sa.Text(), nullable=True))
    op.drop_column('carpools', 'to_point')
    op.drop_column('carpools', 'to_place')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpools', sa.Column('to_place', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('carpools', sa.Column('to_point', geoalchemy2.types.Geometry(geometry_type='POINT'), autoincrement=False, nullable=True))
    op.drop_column('carpools', 'vehicle_description')
    op.drop_column('carpools', 'notes')
    # ### end Alembic commands ###
