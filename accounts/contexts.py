from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def userprofile(request):
    """User Profile"""
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'user_profile': user_profile,
    }

    return context
