from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404

from trips.models import Trip


def view_bag(request):
    """Render bag.htm template"""
    return render(request, 'bag/bag.html',)


def add_to_bag(request, trip_id):
    """
    Add items to the bag
    Check if the trip already exists in the bag
    then update the bag, if does not then add the trip
    to the bag.
    """
    booking_date = request.POST.get('booking_date')
    adult_tickets = int(request.POST.get('adult_tickets'))
    children_tickets = int(0)
    redirect_url = request.POST.get('redirect_url')
    trip = get_object_or_404(Trip, pk=trip_id)

    # Check it the children tickets are in the request
    if 'children_tickets' in request.POST:
        children_tickets = int(request.POST['children_tickets'])
        total_tickets = adult_tickets + children_tickets
    else:
        total_tickets = adult_tickets

    bag = request.session.get('bag', {})

    # Check if the trip is already in the bag
    if trip_id in list(bag.keys()):
        if booking_date == bag[trip_id]['booking_date']:
            bag[trip_id]['quantity'] += 1
            bag[trip_id]['booking_date'] = booking_date
            bag[trip_id]['adult_tickets'] += adult_tickets
            bag[trip_id]['children_tickets'] += children_tickets
            # update number of tickets available for the trip
            if total_tickets <= trip.num_tickets:
                trip.num_tickets -= total_tickets
                trip.save()
                messages.success(request,
                                 (f' Updated suitcase for {trip.name}'
                                  f' and {booking_date} date with'
                                  f' {adult_tickets} adult tickets'
                                  f' and {children_tickets} children tickets'))
            else:
                messages.error(request, f"There are only {trip.num_tickets} "
                                        f"tickets left for this trip")
    else:
        # Check if there are enough tickets
        if total_tickets <= trip.num_tickets:
            trip.num_tickets -= total_tickets
            trip.save()
            bag[trip_id] = {
                'quantity': 1,
                'booking_date': booking_date,
                'adult_tickets': adult_tickets,
                'children_tickets': children_tickets,
            }
            messages.success(request, (f'Added {trip.name},'
                                       f' on {booking_date} to your suitcase'))
        else:
            messages.error(request, f"There are only {trip.num_tickets}"
                                    f" tickets left for this trip")

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, trip_id):
    """
    Update ticket quantity and booking date
    If adult ticket quantity is less then 0
    Delete trip from the bag
    """
    adult_tickets = int(request.POST.get('adult_tickets'))
    children_tickets = int(0)
    booking_date = request.POST.get('booking_date')
    trip = get_object_or_404(Trip, pk=trip_id)

    if 'children_tickets' in request.POST:
        children_tickets = int(request.POST['children_tickets'])

    bag = request.session.get('bag', {})

    if booking_date:
        bag[trip_id]['booking_date'] = booking_date

    if adult_tickets:
        if adult_tickets > 0:
            bag[trip_id]['adult_tickets'] = int(adult_tickets)
            bag[trip_id]['children_tickets'] = int(children_tickets)
        messages.success(request, (f'Updated your booking requirements'
                                   f' for {trip.name}'))
    else:
        del bag[trip_id]
        messages.success(request, (f'Removed {trip.name},'
                                   f'from your suitcase'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, trip_id):
    """
    Remove the trip by trip_id from the bag
    """

    try:
        trip = get_object_or_404(Trip, pk=trip_id)
        bag = request.session.get('bag', {})
        total_tickets = (
            bag[trip_id]['adult_tickets'] + bag[trip_id]['children_tickets']
        )
        trip.num_tickets += total_tickets
        trip.save()
        del bag[trip_id]
        messages.success(request, (f'Removed {trip.name},'
                                   f'from your suitcase'))

        request.session['bag'] = bag

        if not bag:
            return redirect(reverse('trips'))

        return redirect(reverse('view_bag'))
    except Exception as e:
        messages.error(request, f'Error has occured when removing'
                       f' {trip.name} from your suitcase')
        return HttpResponse(status=500, e=e)
