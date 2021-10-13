from django import forms
from .models import Account


class RegistraionForm(forms.ModelForm):
    """
    Registration Form
    """
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password'
    }))

    class Meta:
        """Create a model form"""
        model = Account
        fields = ['first_name', 'last_name', 'phone_number',
                  'email', 'password']

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes to all the input fields"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
