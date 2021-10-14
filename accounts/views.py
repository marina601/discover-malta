from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


# from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import RegistraionForm
from .models import Account

# Create your views here.


# @csrf_exempt
def register(request):
    """
    Register function
    """
    if request.method == 'POST':
        form = RegistraionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name,
                                               last_name=last_name,
                                               email=email,
                                               username=username,
                                               password=password,)
            user.phone_number = phone_number
            user.save()

            # Account activation
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_activation.html', {
                'user': user,
                'domain': current_site,
                # encoding user id
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, f'Thank you {user.first_name} for'
                                      f' registering,'
                                      f' we have send you an email with'
                                      f' verification link.'
                                      f' Please verify your account')
            form = RegistraionForm()
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistraionForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    """
    Login function
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid login details, please try again!")
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    """Logout function"""
    auth.logout(request)
    messages.success(request, "You have logged out!")
    return redirect('profile')


def activate(request, uidb64, token):
    """Activate New User Account"""
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f'Congratulations {user.first_name} your'
                                  f' account has been activated')
        return redirect('login')
    else:
        messages.error(request, "Invalid activation link")
        return redirect('register')


@login_required(login_url='login')
def profile(request):
    """User Profile"""
    return render(request, 'accounts/profile.html')