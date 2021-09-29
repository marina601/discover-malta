from django.forms import ModelForm
from django import forms
from availability.models import Ticket


class AvailabilityForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['trip', 'available_days', 'start_time']
        widgets = {
            'available_days': forms.DateInput(attrs={'class': 'datepicker'}),
        }
