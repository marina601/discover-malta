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
    children_tickets = int(0)
    redirect_url = request.POST.get('redirect_url')
    # trip = get_object_or_404(Trip, pk=trip_id)

    # Check it the children tickets are in the request
    if 'children_tickets' in request.POST:
        children_tickets = int(request.POST['children_tickets'])
    bag = request.session.get('bag', {})

    if trip_id in list(bag.keys()):
        """
        Add items to the bag
        """
        bag[trip_id]['quantity'] += 1
        bag[trip_id]['booking_date'] = booking_date
        bag[trip_id]['adult_tickets'] = adult_tickets
        bag[trip_id]['children_tickets'] = children_tickets
    else:
        bag[trip_id] = {
            'quantity': 1, 'booking_date': booking_date,
            'adult_tickets': adult_tickets,
            'children_tickets': children_tickets,
        }

    request.session['bag'] = bag
    # del request.session['bag']
    print(f'bag is: {bag}')

    return redirect(redirect_url)


def update_bag(request, trip_id):
    """
    Add a quantity of the specific trip
    to the shopping bag
    """
    adult_tickets = int(request.POST.get('adult_tickets'))
    children_tickets = int(0)
   
    # Check it the children tickets are in the request
    # check if adult_tickets exist
    # else delete the trip

    if 'children_tickets' in request.POST:
        children_tickets = int(request.POST['children_tickets'])
    bag = request.session.get('bag', {})

    if adult_tickets:
        if adult_tickets > 0:
            bag[trip_id]['adult_tickets'] = int(adult_tickets)
            bag[trip_id]['children_tickets'] = int(children_tickets)
    else:
        del bag[trip_id]

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
