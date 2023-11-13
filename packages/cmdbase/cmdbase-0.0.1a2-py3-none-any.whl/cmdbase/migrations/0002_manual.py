
from django.db import migrations
from ..utils import get_sql_migration_operations


class Migration(migrations.Migration):
    dependencies = [
        ('cmdbase', '0001_initial'),
    ]

    operations = get_sql_migration_operations()
