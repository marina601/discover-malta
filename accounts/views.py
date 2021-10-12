from django.shortcuts import render

# Create your views here.


def register(request):
    """
    Register function
    """
    return render(request, 'accounts/register.html')


def login(request):
    """
    Login function
    """
    return render(request, 'accounts/login.html')
