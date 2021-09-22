from django.shortcuts import render, get_object_or_404
from .models import Trip, Category

# Create your views here.


def all_trips(request, category_slug=None):
    categories = None
    trips = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        trips = Trip.objects.filter(category=categories)
        result_count = trips.count()
    else:
        """
        Display all trips including sorting and searching queries
        """
        trips = Trip.objects.all()
        result_count = trips.count()

    context = {
        'trips': trips,
        'result_count': result_count,
        'categories': categories,
    }

    return render(request, 'trips/trips.html', context)


# def trip_detail(request, trip_id):
#     """
#     Display a single trip by id
#     """
#     trip = get_object_or_404(Trip, pk=trip_id)

#     context = {
#         'trip': trip,
#     }

#     return render(request, 'trips/trip_detail.html', context)
