# Generated by Django 4.2.13 on 2024-07-30 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brasileirao', '0002_alter_squadindex_last_5_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squadxga',
            old_name='gls',
            new_name='goals',
        ),
        migrations.RenameField(
            model_name='squadxga',
            old_name='ninities',
            new_name='nineties',
        ),
    ]
