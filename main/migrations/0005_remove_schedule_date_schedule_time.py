# Generated by Django 4.1.3 on 2022-11-16 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_title_schedule_direction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время'),
            preserve_default=False,
        ),
    ]