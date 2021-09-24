# Generated by Django 3.2.7 on 2021-09-24 20:02

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0003_auto_20210917_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_days', multiselectfield.db.fields.MultiSelectField(choices=[('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thur', 'Thur'), ('Fri', 'Fri'), ('Sat', 'Sat'), ('Sun', 'Sun')], max_length=28)),
                ('start_time', models.TimeField(default=True)),
                ('tickets_available', models.PositiveIntegerField(default=0)),
                ('provider', models.CharField(blank=True, max_length=50)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip')),
            ],
        ),
    ]
