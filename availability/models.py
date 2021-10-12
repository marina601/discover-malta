from django.db import models
from django.utils import timezone
from trips.models import Trip


# Multi Select Field was used
# from Django Documentations https://pypi.org/project/django-multiselectfield/


class Ticket(models.Model):
    # comes from the trips
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    booking_date = models.DateField(default=timezone.now)
    total_adults = models.PositiveIntegerField(default=0)
    num_of_childen = models.PositiveIntegerField(default=0)
    total_num_tickets = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} {} {}'.format(self.booking_date,
                                 self.total_num_tickets, 
                                 self.total_price)
