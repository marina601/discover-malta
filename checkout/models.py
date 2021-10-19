# pylint: disable=no-member
import uuid
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from django.utils import timezone


from trips.models import Trip
# Create your models here.


class Order(models.Model):
    """Order model"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False, default="")
    last_name = models.CharField(max_length=50, null=False, blank=False, default="")
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    # not required field
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    # not required field
    county = models.CharField(max_length=80, null=True, blank=True)
    # auto_now_add field will automatically set order date and time
    date = models.DateTimeField(auto_now_add=True)
    # these fields will be calculated using the model method
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """Generate unique ticket number"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total price for the order
        """
        self.order_total = self.ticketitems.aggregate(Sum
                                                      ('ticketitem_total')
                                                      )['ticketitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Overwrite the original save method to set
        ticket number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderTicketItem(models.Model):
    """Ticke Item"""
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='ticketitems')
    trip = models.ForeignKey(Trip, null=False, blank=False,
                             on_delete=models.CASCADE)
    booking_date = models.DateField(default=timezone.now)
    children_tickets = models.IntegerField(null=True, blank=True, default=0)
    child_quantity = models.IntegerField(null=True, blank=True, default=0)
    adult_tickets = models.IntegerField(null=False, blank=False, default=0)
    adult_quantity = models.IntegerField(null=False, blank=False, default=0)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    ticketitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                           null=False, blank=False,
                                           editable=False)

    def save(self, *args, **kwargs):
        """
        Calculate total cost of the trip
        """
        self.children_tickets = self.trip.child_price * self.child_quantity
        self.adult_tickets = self.trip.adult_price * self.adult_quantity
        self.ticketitem_total = (self.children_tickets + self.adult_tickets) * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.trip.name} on order {self.order.order_number}'
