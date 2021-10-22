from django import forms
from .models import Category, Trip


class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.items():
            field.widget.attr['class'] = 'form-control'
            self.fields['trip_name'].widget.attrs['autofocus'] = True
