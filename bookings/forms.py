from django.forms import ModelForm
from django import forms
from availability.models import Ticket


class AvailabilityForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['trip', 'booking_date', 'total_adults', 'num_of_childen']
