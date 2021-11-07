from django.contrib import admin
from .models import Category, Trip, ReviewRating


class CategoryAdmin(admin.ModelAdmin):
    """Category Model fields"""
    prepopulated_fields = {
        'slug': ('category_name',)
    }
    list_display = ('category_name', 'slug')


class TripAdmin(admin.ModelAdmin):
    """Trip Model fields"""
    list_display = ('name', 'category', 'provider',
                    'duration', 'departure_location', 'family_friendly',
                    'adult_price', 'child_price', 'num_tickets')
    prepopulated_fields = {'slug': ('name',)}


class ReviewRatingAdmin(admin.ModelAdmin):
    """ReviewRating Model fields"""
    list_display = ('user', 'rating', 'trip')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
