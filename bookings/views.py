from django.shortcuts import render
from .forms import AvailabilityForm

# Create your views here.

def view_availability(request):
    """
    View Availability for a trip
    """
    form = AvailabilityForm()
    
    context = {
        'form': form,
    }
    return render(request, 'bookings/view_availability.html', context)
