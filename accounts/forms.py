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
    phone_number = forms.IntegerField(required=True)

    class Meta:
        """Create a model form"""
        model = Account
        fields = ['first_name', 'last_name',
                  'email', 'password']

    def clean(self):
        """Check the passwords match"""
        cleaned_data = super(RegistraionForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Your passwords do not match")

    def __init__(self, *args, **kwargs):
        """Add bootstrap classes to all the input fields"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
