from django.shortcuts import get_object_or_404
from trips.models import Trip


def bag_content(request):
    """
    Iterate through all the bag items
    and calculate price and quantity
    gettin the values from the booking form
    """

    bag_items = []
    total_price = 0
    total_tickets = 0
    trip_count = 0
    adult_price = 0
    child_price = 0
    bag = request.session.get('bag', {})
    print("ADDED BY JO: bag in contexts.py: ", bag)

    for key, values in bag.items():
        trip = get_object_or_404(Trip, pk=key)
        if "adult_tickets" in bag[key]:
            adult_tickets = bag[key]['adult_tickets']
            adult_price = trip.adult_price * bag[key]['adult_tickets']
            booking_date = bag[key]['booking_date']
            trip_count += bag[key]['quantity']
            total_tickets = adult_tickets
            children_tickets = bag[key]['children_tickets']
            child_price = trip.child_price * children_tickets
            total_price = adult_price + child_price
            total_tickets = adult_tickets + children_tickets
            bag_items.append({
                'trip': trip,
                'total_tickets': total_tickets,
                'adult_price': adult_price,
                'total_price': total_price,
                'trip_count': trip_count,
                'booking_date': booking_date,
                'adult_tickets': adult_tickets,
                'children_tickets': children_tickets,
                'child_price': child_price,
            })

    context = {
        'bag_items': bag_items,
        'total_price': total_price,
        'total_tickets': total_tickets,
    }

    print(context)

    return context
