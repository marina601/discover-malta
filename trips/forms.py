from django import forms
from .models import Trip, ReviewRating


class TripForm(forms.ModelForm):
    """
    Creating a form to add trips to the database
    """
    class Meta:
        model = Trip
        fields = ['name', 'category', 'short_description', 'full_description',
                  'included', 'what_to_bring',
                  'duration', 'start_time', 'departure_location',
                  'family_friendly',
                  'adult_price', 'child_price', 'images', 'num_tickets']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            # Add classes to the form fields
            self.fields[field].widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    """
    Form to submit user trip review and rating
    """
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            # Add classes to the form fields
            self.fields[field].widget.attrs['class'] = 'form-control'
