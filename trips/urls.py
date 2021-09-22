from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trips, name='trips'),
   # path('<trip_id>', views.trip_detail, name='trip_detail'),
    path('<slug:category_slug>/', views.all_trips, name='trips_by_category'),
]
