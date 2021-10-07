
from django.shortcuts import render, redirect, reverse, HttpResponse
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
    # trip = get_object_or_404(Trip, pk=trip_id)
    bag = request.session.get('bag', {})

    if trip_id in list(bag.keys()):
        bag[trip_id]['quantity'] += 1
        bag[trip_id]['booking_date'] = booking_date
        bag[trip_id]['adult_tickets'] = adult_tickets
        bag[trip_id]['children_tickets'] = children_tickets
        print(children_tickets)
    else:
        bag[trip_id] = {
            'quantity': 1, 'booking_date': booking_date, 'adult_tickets': adult_tickets, 'children_tickets': children_tickets
        }

    request.session['bag'] = bag
    # print(children_tickets)
    # print(request.session["bag"])
    return redirect(redirect_url)


def update_bag(request, trip_id):
    """
    Add a quantity of the specific trip
    to the shopping bag
    """

    adult_tickets = int(request.POST.get('adult_tickets'))
    children_tickets = int(request.POST.get('children_tickets'))
    bag = request.session.get('bag', {})

    if adult_tickets > 0:
        bag[trip_id]['adult_tickets'] = int(adult_tickets)
        bag[trip_id]['children_tickets'] = int(children_tickets)
    else:
        del bag[trip_id]['adult_tickets']
        del bag[trip_id]['children_tickets']
    
    if children_tickets > 0:
        bag[trip_id]['children_tickets'] = int(children_tickets)
    else:
        del bag[trip_id]['children_tickets']

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, trip_id):
    """
    Remove all the tickets from bag
    """
    bag = request.session.get('bag', {})

    bag.pop(trip_id)

    request.session['bag'] = bag
    return HttpResponse(status=200)
