# pylint: disable=no-member
from django.test import TestCase
from .models import Trip, Category


class TestTripModels(TestCase):
    """Test Trip App Models"""

    def test_famly_friendly_default_to_true(self):
        """Test the family friendly field is set to True"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        trip = Trip.objects.create(name='Test Trip', duration=5,
                                   category=category, slug='test-trip',
                                   images='image.jpg')
        self.assertTrue(trip.family_friendly)

    def test_favourites_default_false(self):
        """Test trip favourite field is blank as default"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        trip = Trip.objects.create(name='Test Trip', duration=5,
                                   category=category, slug='test-trip',
                                   images='image.jpg')
        self.assertTrue(trip.add_to_favourites)

    def test_trip_string_method_returns_name(self):
        """Test category string method"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        trip = Trip.objects.create(name='Test Trip', duration=5,
                                   category=category, slug='test-trip',
                                   images='image.jpg')
        self.assertEqual(str(trip), 'Test Trip')

class TestCategoryModel(TestCase):
    """Test Category Model"""

    def test_image_default_false(self):
        """Test image field is black"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        self.assertFalse(category.cat_image)
    
    def test_category_string_method_returns_name(self):
        """Test category string method"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        self.assertEqual(str(category), 'Test Category')
        
