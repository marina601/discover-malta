from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_trips, name='trips'),
    path('category/<slug:category_slug>/', views.all_trips,
         name='trips_by_category'),
    path('category/<slug:category_slug>/<slug:trip_slug>/', views.trip_detail,
         name='trip_detail'),
    path('search/', views.search, name='search'),
    path('sort_rating/', views.sort_rating, name='sort_rating'),
    path('sort_family_friendly/', views.sort_family_friendly,
         name='sort_family_friendly'),
    # Trip Managment
    path('add_trip/', views.add_trip, name='add_trip'),
    path('update_trip/<int:trip_id>/', views.update_trip, name='update_trip'),
    path('delete_trip/<int:trip_id>/', views.delete_trip, name='delete_trip'),
    # Reviews
    path('submit_review/<int:trip_id>/<int:user_id>/', views.submit_review,
         name='submit_review'),
    path('delete_review/<int:review_id>/', views.delete_review,
         name='delete_review'),
]
