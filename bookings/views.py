from django.shortcuts import render


from trips.models import Trip
from availability.models import Ticket
# Create your views here.


def view_availability(request, id):
    """
    View Availability for a trip
    """
    trip = Trip.objects.get(id=id)
    
    context = {
        'trip': trip,
    }
    
    return render(request, 'bookings/view_availability.html', context)


def ticket(request):
    """
    Creating a booking
    """


    return render(request, 'add_to_suitcase.html')
