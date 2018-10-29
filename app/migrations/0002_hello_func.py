# Generated by Django 2.2.dev20181026000358 on 2018-10-29 02:26

from django.db import migrations
from django.conf import settings
from pathlib import Path


with Path(settings.BASE_DIR, 'sql/ddl/hello.sql').open() as f:
    CREATE_FUNCTION = f.read().strip()
DROP_FUNCTION = 'DROP FUNCTION hello'


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            [CREATE_FUNCTION],
            DROP_FUNCTION
        )
    ]
