"""empty message

Revision ID: 4416a8676605
Revises: 4b0f722c0ae6
Create Date: 2024-01-16 16:17:17.196428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4416a8676605'
down_revision = '4b0f722c0ae6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('city', schema=None) as batch_op:
        batch_op.drop_constraint('city_country_capital_id_key', type_='unique')
        batch_op.create_unique_constraint(None, ['id'])
        batch_op.drop_constraint('city_country_capital_id_fkey', type_='foreignkey')
        batch_op.drop_column('country_capital_id')

    with op.batch_alter_table('country', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('country', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('city', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country_capital_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('city_country_capital_id_fkey', 'country', ['country_capital_id'], ['id'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('city_country_capital_id_key', ['country_capital_id'])

    # ### end Alembic commands ###
