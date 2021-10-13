from django.shortcuts import render

from .forms import RegistraionForm

# Create your views here.


def register(request):
    """
    Register function
    """
    form = RegistraionForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    """
    Login function
    """
    return render(request, 'accounts/login.html')
