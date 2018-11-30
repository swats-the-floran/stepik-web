# Generated by Django 2.1.2 on 2018-11-29 04:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0002_auto_20181123_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(related_name='q_to_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
