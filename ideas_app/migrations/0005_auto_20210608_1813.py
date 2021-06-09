# Generated by Django 3.2.4 on 2021-06-08 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas_app', '0004_auto_20210608_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50)),
                ('long_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['short_name'],
            },
        ),
        migrations.AlterField(
            model_name='professor',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ideas_app.institute'),
        ),
        migrations.AlterField(
            model_name='researcher',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ideas_app.institute'),
        ),
        migrations.AlterField(
            model_name='residencestudent',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ideas_app.institute'),
        ),
    ]