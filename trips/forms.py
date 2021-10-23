from django import forms
from .models import Trip, Category, ReviewRating


class TripForm(forms.ModelForm):
    """
    Creating a form to add trips to the database
    """

    class Meta:
        model = Trip
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        for field_name, field in self.fields.items():
            """ Add classes to the form fields"""
            field.widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
