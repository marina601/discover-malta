from django.shortcuts import render

# Create your views here.


def bag(request):
    return render(request, 'bag/bag.html',)
