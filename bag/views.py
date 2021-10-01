from django.shortcuts import render, redirect

# Create your views here.


def bag(request):
    return render(request, 'bag/bag.html',)

def add_to_bag(request, trip_id):
    """
    Add a quantity of the specific trip
    to the shopping bag
    """

    booking_date = request.POST.get('booking_date')
    redirect_url = request.POST.get('redirect_url')
    total_adults = int(request.POST.get('total_adults'))
    num_of_childen = request.POST.get('num_of_children')
    bag = request.session.get('bag', {})

    if trip_id in list(bag.keys()):
        bag[trip_id] += total_adults
    else:
        bag[trip_id] = total_adults
    
    request.session['bag'] = bag

    return redirect(redirect_url)

    # Calculate
    # total_num_tickets
    # total_price
