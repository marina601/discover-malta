# pylint: disable=no-member
# pylint: disable=protected-access
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from checkout.models import Order
from trips.models import Trip, ReviewRating
from trips.forms import ReviewForm
from .forms import RegistraionForm, UserProfileForm, UserForm
from .models import Account, UserProfile

# Create your views here.


def register(request):
    """
    Registration functionality, if the form is valid
    create a new user and generate a username
    """
    if request.user.is_authenticated:
        messages.info(request, "You have alredy registered!")
        return redirect('profile')

    if request.method == 'POST':
        form = RegistraionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0] + last_name
            user = Account.objects.create_user(first_name=first_name,
                                               last_name=last_name,
                                               email=email,
                                               username=username,
                                               password=password,)
            user.phone_number = phone_number
            user.save()

            # Send Account activation email
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string(
                    'accounts/emails/account_activation.html', {
                        'user': user,
                        'domain': current_site,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    }
                )
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, f'Thank you {user.first_name} for'
                             f' registering,'
                             f' we have send you an email with'
                             f' verification link.'
                             f' Please verify your account')
            form = RegistraionForm()
            return redirect(
                '/accounts/login/?command=verification&email=' + email)
    else:
        form = RegistraionForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    """
    Login function
    Authenticate the user by email address
    and password
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Welcome {user.first_name}"
                             f" you are now logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid login details, please try again!")
            return redirect('login')

    if request.user.is_authenticated:
        messages.info(request, "You have are already logged in!")
        return redirect('profile')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    """Logout function"""
    auth.logout(request)
    messages.success(request, "You have logged out!")
    return redirect('home')


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
    userprofile = get_object_or_404(UserProfile, user=request.user)
    # display the orders in desc order
    orders = userprofile.orders.all().order_by('-date')

    context = {
        'userprofile': userprofile,
        'orders': orders,
    }

    return render(request, 'accounts/profile.html', context)


def forgot_password(request):
    """
    Forgot password, checks if there is a POST
    request, if the user email is identified
    and sends an email with a link to reset password
    """
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string(
                'accounts/emails/reset_password_email.html', {
                    'user': user,
                    'domain': current_site,
                    # encoding user id
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                }
            )
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, f'Password reset link has been '
                             f'send to {to_email}')
            return redirect('login')
        else:
            messages.error(request, "The email address you have entered does "
                                    "not match any account")
            return redirect('forgot_password')

    return render(request, 'accounts/forgot_password.html')


def validate_new_password(request, uidb64, token):
    """Validate new password request link"""
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, f'Please {user.first_name} you'
                         f' can now reset your password')
        return redirect('reset_password')
    else:
        messages.error(request, "This link has expired, please"
                                " request a new link")
        return redirect('forgot_password')


def reset_password(request):
    """
    Reset user password by
    checking if two passwords match
    and getting uid in session,
    updating user password
    """
    if request.method == 'POST':
        password = request.POST['password-1']
        confirm_password = request.POST['password-2']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, f'{user.first_name} your'
                             f' password has been reset!')
            return redirect('login')
        else:
            messages.warning(request, 'Please ensure your new password'
                                      ' and confirm password match')
            return redirect('reset_passord')
    else:
        return render(request, 'accounts/reset_password.html')


@login_required
def edit_profile(request):
    """Update user profile"""
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES,
                                       instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('edit_profile')
        else:
            messages.error(request, 'We were not able to update your profile.'
                                    'Please ensure all the required '
                                    'fields are complete')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
    return render(request, 'accounts/edit_profile.html', context)


@login_required
def order_history(request, order_number):
    """View past order history"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        f'A confirmation email was send on the order date {order.date}'
    ))

    template = 'checkout/checkout_complete.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_favourite(request, trip_id):
    """Adding Favourites to Users"""
    trip = get_object_or_404(Trip, id=trip_id)
    url = request.META.get('HTTP_REFERER')

    if trip.add_to_favourites.filter(id=request.user.id).exists():
        trip.add_to_favourites.remove(request.user)
        messages.success(request, f"Removed {trip.name} from your favourites")
        return redirect(url)
    else:
        trip.add_to_favourites.add(request.user)
        messages.success(request, f"We have added {trip.name}"
                         " to your favourites")
        return redirect(url)


@login_required
def favourites(request):
    """Display favourite trips"""

    fav_trips = Trip.objects.filter(add_to_favourites=request.user.id)
    fav_result_count = fav_trips.count()

    template = 'accounts/favourites.html'
    context = {
        'fav_trips': fav_trips,
        'fav_result_count': fav_result_count,
    }

    return render(request, template, context)


@login_required
def view_reviews(request):
    """Display All user reviews"""
    reviews = ReviewRating.objects.filter(user=request.user.id)

    template = 'accounts/view_reviews.html'
    context = {
        'reviews': reviews
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """Edit user review"""
    review = get_object_or_404(ReviewRating, pk=review_id)
    form = ReviewForm(instance=review)
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = ReviewForm(request.POST, instance=review)
            form.rating = request.POST.get('rating')
            review.updated_at = timezone.now()
            form.save()
            review.save()
            messages.success(request, 'Thank you! Your review has'
                             ' been updated.')
            return redirect('view_reviews')
        else:
            messages.error(request,
                           f'Failed to update {review.trip}.'
                           f' Please ensure the form is valid.')
            return redirect(url)
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.trip}')

    template = 'accounts/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)
