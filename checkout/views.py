# pylint: disable=no-member
import json
from django.shortcuts import render, reverse, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

import stripe

from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from trips.models import Trip
from bag.contexts import bag_content
from .models import Order, OrderTicketItem
from .forms import OrderForm



@require_POST
def cache_checkout_data(request):
    """Handling save info checkbox"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


def checkout(request):
    """Checkout"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # getting the bag from the session
        bag = request.session.get('bag', {})
        # gettin the form data from the input fields
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            # Generate an order ticket item
            for key, values in bag.items():
                try:
                    trip = get_object_or_404(Trip, pk=key)
                    order_ticket_item = OrderTicketItem(
                        order=order,
                        trip=trip,
                        child_quantity=bag[key]['children_tickets'],
                        adult_quantity=bag[key]['adult_tickets'],
                        booking_date=bag[key]['booking_date'],
                        quantity=bag[key]['quantity'],
                    )
                    order_ticket_item.save()
                except Trip.DoesNotExist:
                    # If the trip does not exists
                    messages.error(request, "One of the trips in your suitcase"
                                   " was not found in out database."
                                   "Please contact"
                                   " us for assistance")
                    order.delete()
                    return redirect(reverse('bag'))

            # Check if the check box was ticked
            request.session['save_info'] = 'save-info' in request.POST

            # Send confirmation email
            current_site = get_current_site(request)
            mail_subject = 'Your order confirmation'
            message = render_to_string('checkout/emails/confirmation_email.txt', {
                'order': order,
                'domain': current_site,
            })
            to_email = order.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            return redirect(reverse('checkout_complete', args=[order.order_number]))
        else:
            # if form is not valid
            messages.error(request, "There was an error with your form"
                                    "Please double check our information")
    else:
        # if the bag is empty
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "You do not have any items in your"
                                    " bag at the moment")
            return redirect(reverse('trips'))

        current_bag = bag_content(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Pre fill the form if the user is authenticated
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.user.first_name,
                    'last_name': profile.user.last_name,
                    'email': profile.user.email,
                    'phone_number': profile.user.phone_number,
                    'country': profile.country,
                    'postcode': profile.postcode,
                    'town_or_city': profile.town_or_city,
                    'street_address1': profile.street_address1,
                    'street_address2': profile.street_address2,
                    'county': profile.county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Set up your public key')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_complete(request, order_number):
    """Handle successful checkout"""

    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        userprofile = get_object_or_404(UserProfile, user=request.user)
        order.user_profile = userprofile
        order.save()
    
        # Save the user's info if the checkbox is ticked
        save_info = request.session['save_info']
        if save_info:
            profile_data = {
                'country': order.country,
                'postcode': order.postcode,
                'town_or_city': order.town_or_city,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county': order.county,
            }
            profile_form = UserProfileForm(profile_data, instance=userprofile)
            # Not to overwrite the user image field
            profile_form.profile_img = userprofile.profile_img
            if profile_form.is_valid():
                profile_form.save()

    messages.success(request, f'Your order has been successfuly prcessed! \
                              Your ticket number is {order_number}. \
                                   A confirmation \
                              email will be sent to {order.email}.')
    # delete the shopping bag from this session
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_complete.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
