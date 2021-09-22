from django.db import models
from django.urls import reverse

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
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # cascade will delete all the products if the category is deleted
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # possible foregain key
    provider = models.CharField(max_length=50, blank=True)
    short_description = models.TextField(max_length=300,
                                         help_text='Enter a short description'
                                         'max 150 characters')
    full_description = models.TextField(max_length=800)
    included = models.TextField(max_length=800, blank=True)
    what_to_bring = models.TextField(max_length=800, blank=True)
    duration = models.IntegerField()
    start_time = models.TimeField(default=True)
    departure_location = models.TextField(max_length=800)
    # foregain key for tickets
    family_friendly = models.BooleanField(default=True)
    # foregain key for profile
    add_to_favourites = models.BooleanField(default=False, blank=True)
    adult_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    child_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    images = models.ImageField(upload_to='media/trips')
    image_url = models.URLField(max_length=1024, blank=True)
    num_tickets = models.PositiveIntegerField(default=0)
    # checkbox for special offers
    special_offer = models.BooleanField(default=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
