from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Order Form"""

    class Meta:
        """Order Form Fields"""
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country', 'county', )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # form fields
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Autofocus attribute on the full_name field as true
        # The cursor will start on this field when the user loads the page
        self.fields['first_name'].widget.attrs['autofocus'] = True
        """
        Iterate through form fields and add * if
        the fields are required on the model
        """
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Setting placeholder to the values above
                self.fields[field].widget.attrs['placeholder'] = placeholder
                # adding a css class
            self.fields[field].widget.attrs['class'] = (
                'form-control stripe-style-input'
            )
            # removing the form fields label
            self.fields[field].label = False
