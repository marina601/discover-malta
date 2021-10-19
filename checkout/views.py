from django.shortcuts import render, reverse, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.shortcuts import get_object_or_404
from datetime import datetime

from .models import Order, OrderTicketItem
from .forms import OrderForm
from bag.contexts import bag_content
from django.conf import settings
from trips.models import Trip
# Create your views here.

import stripe
import json


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
            return redirect(reverse('checkout_complete', args=[order.order_number]))
        else:
            # if form is not valid
            messages.error(request, "There was an error with your form"
                                    "Please double check our information")
    else:
        # if the bag is empty
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "You do not have any items in your bag at the moment")
            return redirect(reverse('trips'))
        
        current_bag = bag_content(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # print(intent)
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

    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order has been successfuly prcessed! \
                              Your ticket number is {order_number}. A confirmation \
                              email will be sent to {order.email}.')
    # delete the shopping bag from this session
    if 'bag' in request.session:
        del request.session['bag']
    
    template = 'checkout/checkout_complete.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
