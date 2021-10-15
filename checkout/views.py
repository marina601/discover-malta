from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .models import Order, OrderTicketItem
from .forms import OrderForm
# Create your views here.


def checkout(request):
    """Checkout"""
    bag = request.session.get('bag', {})
    if not bag:
        # If the bag is empty
        messages.error(request, "You do not have any items in your bag at the moment")
        return redirect(reverse('trips'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
    
