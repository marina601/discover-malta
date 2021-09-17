from django.contrib import admin
from .models import Category, Trip

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('category_name',)
    }
    list_display = ('category_name', 'slug')


class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider',
                    'duration', 'departure_location', 'family_friendly',
                    'adult_price', 'child_price', 'num_tickets')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Trip, TripAdmin)
