# Generated by Django 4.2.1 on 2023-05-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mba_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='rank',
            field=models.CharField(max_length=255),
        ),
    ]
