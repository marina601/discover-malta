from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q


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
        # get all the trips by category slug
        categories = get_object_or_404(Category, slug=category_slug)
        trips = Trip.objects.filter(category=categories)
        # pagination
        paginator = Paginator(trips, 2)
        page = request.GET.get('page')
        paged_trips = paginator.get_page(page)
        # trip count
        result_count = trips.count()
    else:
        # get all the trips
        trips = Trip.objects.all()
        # pagination
        paginator = Paginator(trips, 8)
        page = request.GET.get('page')
        paged_trips = paginator.get_page(page)
        # trip count
        result_count = trips.count()


    context = {
        'trips': paged_trips,
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


def search(request):
    trips = None
    trips_count = None
    query = None
    """
    Search function, cheking if the method is GET
    and the keyword=name in input, store the value
    """
    if 'q' in request.GET:
        keyword = request.GET['q']
        if keyword:
            trips = Trip.objects.order_by('-created_date').filter(Q(full_description__icontains=keyword) | Q(name__icontains=keyword))
            result_count = trips.count()
        else:
            messages.error(request, "You didn't enter any serach criteria! ")
            return redirect(reverse('trips'))
    
    context = {
        'trips': trips,
        'result_count': result_count,
    }

    return render(request, 'trips/trips.html', context)
