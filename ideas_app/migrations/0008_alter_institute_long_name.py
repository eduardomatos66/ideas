# Generated by Django 3.2.4 on 2021-06-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas_app', '0007_auto_20210609_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='long_name',
            field=models.CharField(max_length=200),
        ),
    ]
