# Generated by Django 4.2.13 on 2024-07-30 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brasileirao', '0004_rename_minutes_played_playernpgxg_nineties'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passing',
            options={'ordering': ['-xa']},
        ),
        migrations.RenameField(
            model_name='passing',
            old_name='progressive_passes',
            new_name='prgp',
        ),
        migrations.RenameField(
            model_name='passing',
            old_name='x_a',
            new_name='xa',
        ),
    ]
