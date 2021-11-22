# pylint: disable=no-member
from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import Account


class Category (models.Model):
    """Category Model"""
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='media/categories', blank=True)

    class Meta:
        """Modify Plural Name"""
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        """url for categories"""
        return reverse('trips_by_category', args=[self.slug])

    def __str__(self):
        return str(self.category_name)


class Trip(models.Model):
    """Trip Model"""

    START_TIME = [
        ('06:00', '06:00'),
        ('07:00', '07:00'),
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('18:00', '18:00'),
    ]

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    provider = models.CharField(max_length=50, blank=True)
    short_description = models.TextField(max_length=300,
                                         help_text='Enter a short description'
                                         'max 300 characters')
    full_description = models.TextField(max_length=800)
    included = models.TextField(max_length=800, blank=True)
    what_to_bring = models.TextField(max_length=800, blank=True)
    duration = models.IntegerField()
    start_time = models.CharField(
        max_length=5,
        choices=START_TIME, default='08:00',
    )
    departure_location = models.TextField(max_length=800)
    family_friendly = models.BooleanField(default=True)
    add_to_favourites = models.ManyToManyField(Account,
                                               related_name='favourites',
                                               default=None, blank=True)
    adult_price = models.DecimalField(max_digits=6, decimal_places=2,
                                      default=0.0)
    child_price = models.DecimalField(max_digits=6, decimal_places=2,
                                      default=0.0)
    images = models.ImageField(upload_to='media/trips')
    num_tickets = models.PositiveIntegerField(default=0)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    special_offer = models.BooleanField(default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        """url for trip detail"""
        return reverse('trip_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return str(self.name)

    def averageRating(self):
        """Calculate average trip review"""
        reviews = ReviewRating.objects.filter(trip=self,
                                              status=True).aggregate(
                                                  average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def totalReviews(self):
        """Calculate total reviews"""
        reviews = ReviewRating.objects.filter(trip=self,
                                              status=True).aggregate(
                                                  count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count


class ReviewRating(models.Model):
    """Rating and Review Model"""
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    review = models.TextField(max_length=500, blank=True,)
    rating = models.FloatField(blank=False, validators=[
                                            MinValueValidator(0.5),
                                            MaxValueValidator(5.0)
                                            ])
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(ReviewRating, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.subject)
