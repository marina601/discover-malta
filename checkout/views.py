from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .models import Order, OrderTicketItem
from .forms import OrderForm
from bag.contexts import bag_content
from django.conf import settings
# Create your views here.

import stripe

def checkout(request):
    """Checkout"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # getting the bag from the session
    bag = request.session.get('bag', {})
    if not bag:
        # If the bag is empty
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

    print(intent)

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
    
