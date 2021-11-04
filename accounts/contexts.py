# pylint: disable=no-member
from trips.models import Trip


def favourites_list(request):
    """Getting the favourites count"""

    fav_trips = Trip.objects.filter(add_to_favourites=request.user.id)
    fav_result_count = fav_trips.count()

    context = {
        'fav_trips': fav_trips,
        'fav_result_count': fav_result_count,
    }

    return context
