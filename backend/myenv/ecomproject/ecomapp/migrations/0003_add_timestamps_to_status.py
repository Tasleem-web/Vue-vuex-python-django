# Generated migration to add missing timestamp columns to Status table

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_alter_member_status_status'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE ecomapp_status ADD COLUMN created_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);",
            reverse_sql="ALTER TABLE ecomapp_status DROP COLUMN created_at;",
        ),
        migrations.RunSQL(
            "ALTER TABLE ecomapp_status ADD COLUMN updated_at datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);",
            reverse_sql="ALTER TABLE ecomapp_status DROP COLUMN updated_at;",
        ),
    ]
