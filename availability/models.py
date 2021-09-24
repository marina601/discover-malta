from django.db import models
from multiselectfield import MultiSelectField
from trips.models import Trip


# Multi Select Field was used
# from Django Documentations https://pypi.org/project/django-multiselectfield/


class Ticket(models.Model):
    DAYS_OF_THE_WEEK = (
        ('Mon', 'Mon'),
        ('Tue', 'Tue'),
        ('Wed', 'Wed'),
        ('Thur', 'Thur'),
        ('Fri', 'Fri'),
        ('Sat', 'Sat'),
        ('Sun', 'Sun'),
    )
   
    # comes from the trips
    trip = models.ForeignKey('trips.Trip', on_delete=models.CASCADE)
    available_days = MultiSelectField(choices=DAYS_OF_THE_WEEK)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    tickets_available = models.PositiveIntegerField(default=0)
    # could be from the user model
    provider = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.available_days, self.start_time, self.start_time)
