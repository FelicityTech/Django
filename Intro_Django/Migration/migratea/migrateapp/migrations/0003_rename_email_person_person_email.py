# Generated by Django 3.2.12 on 2023-04-10 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrateapp', '0002_rename_name_person_person_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='email',
            new_name='Person_email',
        ),
    ]
