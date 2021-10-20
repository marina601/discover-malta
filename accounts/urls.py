from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('validate_new_password/<uidb64>/<token>', views.validate_new_password,
         name='validate_new_password'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('edit_profile', views.edit_profile, name='edit_profile')
]
