"""
Initial migration for test_applied_migrations app
"""

from tortoise_pathway.migration import Migration
from tortoise_pathway.operations import CreateModel
from tortoise.fields.data import BooleanField
from tortoise.fields.data import CharField
from tortoise.fields.data import DatetimeField
from tortoise.fields.data import DecimalField
from tortoise.fields.data import IntField
from tortoise.fields.data import TextField


class InitialMigration(Migration):
    """
    Initial migration creating products and categories tables.
    """

    dependencies = []
    operations = [
        CreateModel(
            model="test_applied_migrations.Product",
            fields={
                "id": IntField(primary_key=True),
                "name": CharField(max_length=255),
                "description": TextField(),
                "price": DecimalField(max_digits=10, decimal_places=2),
                "is_active": BooleanField(default=True),
                "created_at": DatetimeField(auto_now_add=True),
            },
        ),
        CreateModel(
            model="test_applied_migrations.Category",
            fields={
                "id": IntField(primary_key=True),
                "name": CharField(max_length=100),
                "description": TextField(null=True),
            },
        ),
    ]
