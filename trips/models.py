from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils import timezone

from accounts.models import Account

# Create your models here.


class Category (models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='media/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('trips_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name


class Trip(models.Model):

    START_TIME = [
        ('6 AM', '6 AM'),
        ('7 AM', '7 AM'),
        ('8 AM', '8 AM'),
        ('9 AM', '9 AM'),
        ('10 AM', '10 AM'),
        ('12 PM', '12 PM'),
        ('1 PM', '1 PM'),
        ('6 PM', '6 PM'),
    ]

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    provider = models.CharField(max_length=50, blank=True)
    short_description = models.TextField(max_length=300,
                                         help_text='Enter a short description'
                                         'max 150 characters')
    full_description = models.TextField(max_length=800)
    included = models.TextField(max_length=800, blank=True)
    what_to_bring = models.TextField(max_length=800, blank=True)
    duration = models.IntegerField()
    start_time = models.CharField(
        max_length=5,
        choices=START_TIME, default='8AM',
    )
    departure_location = models.TextField(max_length=800)
    family_friendly = models.BooleanField(default=True)
    add_to_favourites = models.BooleanField(default=False, blank=True)
    adult_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    child_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    images = models.ImageField(upload_to='media/trips')
    num_tickets = models.PositiveIntegerField(default=0)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    special_offer = models.BooleanField(default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('trip_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name
    
    def averageRating(self):
        # Calculate average trip review
        reviews = ReviewRating.objects.filter(trip=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def totalReviews(self):
        # Calculate total reviews
        reviews = ReviewRating.objects.filter(trip=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count



class ReviewRating(models.Model):
    """Rating and Review Model"""
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
