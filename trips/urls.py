from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trips, name='trips'),
    path('category/<slug:category_slug>/', views.all_trips, name='trips_by_category'),
    path('category/<slug:category_slug>/<slug:trip_slug>/', views.trip_detail, name='trip_detail'),
    path('search/', views.search, name='search'),
    path('add_trip/', views.add_trip, name='add_trip'),
    path('submit_review/<int:trip_id>/<int:user_id>/', views.submit_review, name='submit_review'),
]
