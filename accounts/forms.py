from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .models import Account


class RegistraionForm(forms.ModelForm):
    """
    Registration Form
    """
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        """Create a model form"""
        model = Account
        fields = ['first_name', 'last_name',
                  'email', 'password']

    def validate(self, password):
        """Validate password min length"""
        if len(password) < password.min_length:
            raise ValidationError(
                _("This password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': password.min_length},
            )

    def get_help_text(self, password):
        return _(
            "Your password must contain at least %(min_length)d characters."
            % {'min_length': password.min_length}
        )
    
    def clean(self):
        """Check the passwords match"""
        cleaned_data = super(RegistraionForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Your passwords do not match")

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes
        and placeholders to all the input fields
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'first_name': 'Pleas enter your first name',
            'last_name': 'Please enter your last name',
            'email': 'Please enter your email address',
            'phone_number': 'Please enter your phone number',
            'password': 'Create your password',
            'confirm_password': 'Confirm your password',
        }
        for field in self.fields:
            if self.fields[field].required:
                # Adding a * to required fields
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # add placeholders
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # set auto focus
            self.fields['first_name'].widget.attrs['autofocus'] = True
            # set bootstrap class to input fields
            self.fields[field].widget.attrs['class'] = 'form-control'
