from django.shortcuts import render
from .models import Trip, Category

# Create your views here.


def all_trips(request):
    """
    Display all trips including sorting and searching queries
    """
    trips = Trip.objects.all()

    context = {
        'trips': trips,
    }

    return render(request, 'trips/trips.html', context)
