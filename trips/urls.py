from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trips, name='trips'),
    path('<slug:category_slug>/', views.all_trips, name='trips_by_category'),
    path('<slug:category_slug>/<slug:trip_slug>/', views.trip_detail, name='trip_detail'),
    path('search/', views.search, name='search'),
]
