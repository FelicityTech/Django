# Generated by Django 3.2.12 on 2023-04-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrateapp', '0002_rename_course_menuitems_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='name',
            new_name='itemname',
        ),
    ]
