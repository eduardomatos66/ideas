# Generated by Django 3.2.4 on 2021-06-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas_app', '0005_auto_20210608_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='short_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
