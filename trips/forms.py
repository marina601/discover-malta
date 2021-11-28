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
        # Create cutom placeholders
        placeholders = {
            'name': 'Please enter trip name',
            'short_description': 'Enter a short description '
                                 'max 300 characters',
            'full_description': 'Enter a full description max 800 characters',
            'included': 'Enter what is included in the trip',
            'what_to_bring': 'Enter what the user should bring to this trip',
            'duration': 'How long will this trip last',
            'departure_location': 'Please enter a departure/pick-up location',
            'adult_price': 'Adult ticket price',
            'child_price': 'If family friendly, child ticket price',
            'num_tickets': 'Please enter the number of tickets'
                           ' available for sale',
            'family_friendly': 'Are children allowed on this trip?',
        }

        for field in self.fields:
            if field != 'category':
                if field != 'images':
                    if field != 'start_time':
                        if self.fields[field].required:
                            placeholder = f'{placeholders[field]} *'
                        else:
                            placeholder = placeholders[field]
                        # Setting placeholder to the values above
                        self.fields[field].widget.attrs['placeholder'] = (
                                                                    placeholder
                                                                    )
            # Add classes to the form fields
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['adult_price'].widget.attrs['min'] = 0.0
            self.fields['child_price'].widget.attrs['min'] = 0.0


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
            self.fields['subject'].required = True
