# pylint: disable=no-member
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q

from accounts.models import Account
from checkout.models import Order, OrderTicketItem

from .models import Trip, Category, ReviewRating
from .forms import TripForm, ReviewForm
# Create your views here.


def all_trips(request, category_slug=None):
    """
    Display all trips
    Sort Trips by Categories
    Show Trip cound upon query results
    """
    categories = None
    trips = Trip.objects.all()

    if category_slug != None:
        # get all the trips by category slug
        categories = get_object_or_404(Category, slug=category_slug)
        trips = Trip.objects.filter(category=categories)
        # pagination
        paginator = Paginator(trips, 3)
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
        messages.error(request, 'Error has occured processing your request,'
                                ' please try again')
        raise e

    # Show all the reviews on the page 
    reviews = ReviewRating.objects.filter(trip_id=trip.id, status=True)

    context = {
        'trip': trip,
        'reviews': reviews,
    }

    return render(request, 'trips/trip_detail.html', context)


def search(request):
    """Search and sort functionality"""
    trips = None
    sort = None
    direction = None
    result_count = 0

    if request.GET:
        """
        Sorting the trips by name
        in descending or ascending order
        """
        if 'sort' in request.GET:
            trips = Trip.objects.all()
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                trips = trips.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            trips = trips.order_by(sortkey)
            result_count = trips.count()

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
            return redirect(reverse('trips'))

    current_sorting = f'{sort}_{direction}'

    context = {
        'trips': trips,
        'result_count': result_count,
        'current_sorting': current_sorting,
    }

    return render(request, 'trips/trips.html', context)


def add_trip(request):
    """Add a trip to the database"""
    if request.method == 'POST':
        form = TripForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new trip!')
            return redirect(reverse('add_trip'))
        else:
            messages.error(request, 'Failed to add a trip. Please ensure the'
                           ' all the required fields are completed!')
    else:
        form = TripForm()

    template = 'trips/add_trip.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def submit_review(request, trip_id, user_id):
    """
    Allow the review only if the user already purchased the trip
    Check if the review already exists
    and update, 
    otherwise create a new review
    """
    trip = get_object_or_404(Trip, pk=trip_id)
    user = get_object_or_404(Account, pk=user_id)
    url = request.META.get('HTTP_REFERER')
    ticket_purchase = OrderTicketItem.objects.filter(trip=trip.id, order__user_profile__user=request.user)


    if request.method == "POST":
        if ticket_purchase:
            try:
                reviews = ReviewRating.objects.get(user__id=user_id,
                                                   trip__id=trip_id)
                form = ReviewForm(request.POST, instance=reviews)
                form.save()
                messages.success(request, 'Thank you! Your review has'
                                 ' been updated.')
                return redirect(url)
            except ReviewRating.DoesNotExist:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    data = ReviewRating()
                    data.subject = form.cleaned_data['subject']
                    data.review = form.cleaned_data['review']
                    data.rating = form.cleaned_data['rating']
                    data.ip = request.META.get('REMOTE_ADDR')  # will store ip address
                    data.trip = trip
                    data.user = user
                    data.save()
                    messages.success(request, 'Thank you, your review has'
                                              'been submited')
                    return redirect(url)
        else:
            messages.error(request, "You must purchase the trip befor submitting your review")
            return redirect(url)
    