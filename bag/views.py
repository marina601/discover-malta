
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from trips.models import Trip

# Create your views here.


def bag(request):
    return render(request, 'bag/bag.html',)


def add_to_bag(request, trip_id):
    """
    Add a quantity of the specific trip
    to the shopping bag
    """
    booking_date = request.POST.get('booking_date')
    adult_tickets = int(request.POST.get('adult_tickets'))
    children_tickets = int(request.POST.get('children_tickets'))
    redirect_url = request.POST.get('redirect_url')
    trip = get_object_or_404(Trip, pk=trip_id)
    bag = request.session.get('bag', {})

    if trip_id in list(bag.keys()):
        bag[trip_id]['quantity'] += 1
        bag[trip_id]['booking_date'] = booking_date
        bag[trip_id]['adult_ticket'] = adult_tickets
        bag[trip_id]['children_tickets'] = children_tickets
    else:
        bag[trip_id] = {
            'quantity': 1, 'booking_date': booking_date, 'adult_tickets': adult_tickets, 'children_tickets': children_tickets
            }
        
    request.session['bag'] = bag
    print(request.session["bag"])
    return redirect(redirect_url)

    # Calculate
    # total_num_tickets
    # total_price
