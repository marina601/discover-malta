from django.shortcuts import get_object_or_404
from trips.models import Trip
from availability.models import Ticket


def bag_content(request):

    bag_items = []
    total_price = 0
    total_tickets = 0
    ticket = []
    bag = request.session.get('bag', {})

    for trip_id, quantity in bag.items():
        trip = get_object_or_404(Trip, pk=trip_id)
        ticket = get_object_or_404(Ticket)
        adult_price = trip.adult_price * ticket.total_adults
        child_price = trip.child_price * ticket.num_of_childen
        total_price += adult_price + child_price
        total_tickets += ticket.total_adults + ticket.num_of_childen
        bag_items.append({
            'trip_id': trip_id,
            'total_price': total_price,
            'quantity': quantity,
            'total_tickets': total_tickets,
            'trip': trip,
            'ticket': ticket,
        })
     
    context = {
        'bag_items': bag_items,
        'total_price': total_price,
        'total_tickets': total_tickets,
    }

    return context
