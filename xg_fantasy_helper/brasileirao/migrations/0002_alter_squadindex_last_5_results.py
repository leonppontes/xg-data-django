# Generated by Django 4.2.13 on 2024-07-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brasileirao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squadindex',
            name='last_5_results',
            field=models.CharField(max_length=20),
        ),
    ]
