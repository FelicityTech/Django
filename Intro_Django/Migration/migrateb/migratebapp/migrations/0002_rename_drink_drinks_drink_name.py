# Generated by Django 3.2.12 on 2023-04-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migratebapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinks',
            old_name='drink',
            new_name='drink_name',
        ),
    ]
