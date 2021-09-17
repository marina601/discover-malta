from django.shortcuts import render
from trips.models import Category

# Create your views here.


def index(request):
    """ A view to return the index page"""

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'home/index.html', context)
