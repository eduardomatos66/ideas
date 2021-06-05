# Generated by Django 3.2.4 on 2021-06-05 21:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ideas_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='ResidenceStudent',
        ),
        migrations.AlterModelOptions(
            name='devtoolsproject',
            options={'ordering': ['idea_key', 'monograph_key', 'research_key', 'tool_key', 'tool_name', 'status', 'start_date', 'due_date', 'devs']},
        ),
        migrations.AlterModelOptions(
            name='idea',
            options={'ordering': ['key', 'progress', 'priority', 'register_date']},
        ),
        migrations.AlterModelOptions(
            name='linkaddress',
            options={'ordering': ['url']},
        ),
        migrations.AlterModelOptions(
            name='monographinfo',
            options={'ordering': ['monograph_key', 'idea_key', 'title', 'residence_class', 'student', 'professor']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'ordering': ['person']},
        ),
        migrations.AlterModelOptions(
            name='researcher',
            options={'ordering': ['person', 'institution', 'team_org']},
        ),
        migrations.AlterModelOptions(
            name='researchinfo',
            options={'ordering': ['research_key', 'idea_key', 'title', 'progress', 'professor', 'start_date', 'due_date', 'group']},
        ),
        migrations.AlterModelOptions(
            name='residencestudent',
            options={'ordering': ['person']},
        ),
        migrations.AddField(
            model_name='devtoolsproject',
            name='tool_key',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='devtoolsproject',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='devtoolsproject',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='idea',
            name='register_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='researchinfo',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='researchinfo',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]