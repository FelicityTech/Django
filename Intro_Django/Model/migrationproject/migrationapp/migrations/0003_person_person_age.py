# Generated by Django 3.2.12 on 2023-04-05 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('migrationapp', '0002_rename_name_person_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Person_age',
            field=models.CharField(default=django.utils.timezone.now, max_length=3),
            preserve_default=False,
        ),
    ]
