from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('remove/<trip_id>/', views.remove_from_bag, name='remove_from_bag'),
]
