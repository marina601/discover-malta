# Generated by Django 3.2.7 on 2021-10-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.FloatField(blank=True),
        ),
    ]