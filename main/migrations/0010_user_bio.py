# Generated by Django 4.1.3 on 2022-11-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_subscription_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Биография'),
        ),
    ]