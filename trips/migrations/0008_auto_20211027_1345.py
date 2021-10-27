# Generated by Django 3.2.7 on 2021-10-27 11:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0007_alter_reviewrating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='add_to_favourites',
        ),
        migrations.AddField(
            model_name='trip',
            name='add_to_favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
