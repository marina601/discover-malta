from django.shortcuts import render, get_object_or_404
from .models import Trip, Category

# Create your views here.


def all_trips(request):
    """
    Display all trips including sorting and searching queries
    """
    trips = Trip.objects.all()
    categoris = Category.objects.all()

    context = {
        'trips': trips,
        'categories': categoris,
    }

    return render(request, 'trips/trips.html', context)


def trip_detail(request, trip_id):
    """
    Display a single trip by id
    """
    trip = get_object_or_404(Trip, pk=trip_id)

    context = {
        'trip': trip,
    }

    return render(request, 'trips/trip_detail.html', context)
