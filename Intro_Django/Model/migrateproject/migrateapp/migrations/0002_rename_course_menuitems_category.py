# Generated by Django 3.2.12 on 2023-04-06 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrateapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='course',
            new_name='category',
        ),
    ]
