from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/view_availability/', views.view_availability, name='view_availability'), 
]
