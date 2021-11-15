from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .models import Account, UserProfile


class RegistraionForm(forms.ModelForm):
    """
    Registration Form
    """
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.IntegerField(required=True)

    class Meta:
        """Create a RegistrationForm using Account model"""
        model = Account
        fields = ['first_name', 'last_name',
                  'email', 'password']

    # code for password validation has been sorced from
    # https://docs.djangoproject.com/en/3.2/topics/auth/passwords/
    def validate(self, password):
        """Validate password min length"""
        if len(password) < password.min_length:
            raise ValidationError(
                _("This password must contain at least "
                  "%(min_length)d characters."),
                code='password_too_short',
                params={'min_length': password.min_length},
            )

    def get_help_text(self, password):
        """Show the error message to the user on validation"""
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
            'first_name': 'Please enter your name',
            'last_name': 'Please enter your surname',
            'email': 'Please enter your email',
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


class UserForm(forms.ModelForm):
    """User form"""
    class Meta:
        """Create a UserForm using Account model"""
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'email')

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes to
        all the input fields
        """
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            # set auto focus
            self.fields['first_name'].widget.attrs['autofocus'] = True
            # set bootstrap class to input fields
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    """User Profile Form"""
    profile_img = forms.ImageField(required=False,
                                   error_messages={'invalid':
                                                   ("Image files only")
                                                   },
                                   widget=forms.FileInput())

    class Meta:
        """Getting the fields from UserProfiel Model"""
        model = UserProfile
        fields = ('street_address1', 'street_address2', 'town_or_city',
                  'county', 'postcode', 'country', 'profile_img')

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes
        and placeholders to all the input fields
        """
        super(UserProfileForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            # set bootstrap class to input fields
            self.fields[field].widget.attrs['class'] = 'form-control'
