from django.shortcuts import render

# Create your views here.

def view_availability(request):
    """
    View Availability for a trip
    """
    return render(request, 'bookings/view_availability.html')
