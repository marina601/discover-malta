# Generated by Django 3.2.7 on 2021-10-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, default='default_user.png', upload_to='user_profile/'),
        ),
    ]
