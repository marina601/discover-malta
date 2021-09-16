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
                    'duration', 'departure_location', 'family_friendly', 'price',
                    'num_tickets', 'days_available')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Trip, TripAdmin)
