from django.db import models

# Create your models here.


class Category (models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Trip(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # cascade will delete all the products if the category is deleted
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # possible foregain key
    provider = models.CharField(max_length=50, blank=True)
    short_description = models.TextField(max_length=150,
                                         help_text='Enter a short description'
                                         'max 150 characters')
    full_description = models.TextField(max_length=800)
    included = models.TextField(max_length=800, blank=True)
    what_to_bring = models.TextField(max_length=800, blank=True)
    duration = models.IntegerField()
    start_time = models.IntegerField()
    departure_location = models.TextField(max_length=800)
    # foregain key for tickets 
    family_friendly = models.BooleanField(default=True)
    # foregain key for profile
    add_to_favourites = models.BooleanField(default=False, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    images = models.ImageField(upload_to='media')
    days_available = models.DateField()
    num_tickets = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
