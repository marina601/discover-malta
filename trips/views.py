from django.shortcuts import render, get_object_or_404
from .models import Trip, Category

# Create your views here.


def all_trips(request, category_slug=None):
    """
    Display all trips
    Sort Trips by Categories
    Show Trip cound upon query results
    """
    categories = None
    trips = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        trips = Trip.objects.filter(category=categories)
        result_count = trips.count()
    else:
        trips = Trip.objects.all()
        result_count = trips.count()

    context = {
        'trips': trips,
        'result_count': result_count,
        'categories': categories,
    }

    return render(request, 'trips/trips.html', context)


def trip_detail(request, category_slug, trip_slug):
    """
    Display a single trip by category_slug and trip slug
    """
    try:
        trip = Trip.objects.get(category__slug=category_slug,
                                             slug=trip_slug)
    except Exception as e:
        raise e
    
    context = {
        'trip': trip,
    }
  
    return render(request, 'trips/trip_detail.html', context)
