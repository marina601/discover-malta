# pylint: disable=no-member
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import resolve
from .models import Trip, Category
from accounts.models import Account


class TestTripView(TestCase):

    def test_all_trips_view(self):
        """Test all_trips HTTP Response"""
        response = self.client.get('/trips/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips/trips.html')

    def test_trip_details_view(self):
        """Test: Trip Detail HTTP Response"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        trip = Trip.objects.create(name='Test Trip', duration=5,
                                   category=category, slug='test-trip', images='image.jpg')
        response = self.client.get(f'/trips/category/{category.slug}/{trip.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips/trip_detail.html')
    
    def test_get_trip_query(self):
        """Test returning a trip query"""
        response = self.client.get('/trips/', {'q': 'sea'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trips/trips.html")
    
    def test_get_trip_sort_query(self):
        """Test returning a trip sort query"""
        response = self.client.get('/trips/', {'sort': 'adutt_price', 'direction': 'asc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trips/trips.html")
    
    def test_get_sort_family_friendly(self):
        """Test returning a trip query"""
        response = self.client.get('/trips/sort_family_friendly/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trips/trips.html")

    def test_get_sort_rating(self):
        """Test returning a trip query"""
        response = self.client.get('/trips/sort_rating/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trips/trips.html")
    
    def test_get_trip_query_blank(self):
        """Test returning a blank product query"""
        response = self.client.get('/trips/', {'q': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trips/trips.html")
    
    def test_resolve_add_trip(self):
        """Test resolving add trip view"""
        found = resolve('/trips/add_trip/')
        self.assertEqual(found.url_name, "add_trip")
    
    def test_resolve_update_trip(self):
        """Test Updating a Trip"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        trip = Trip.objects.create(name='Test Trip', duration=5,
                                   category=category, slug='test-trip', images='image.jpg')
        found = resolve(f'/trips/update_trip/{trip.id}/')
        self.assertEqual(found.url_name, "update_trip")
        response = self.client.get(f'/trips/update_trip/{trip.id}/')
        self.assertEqual(response.status_code, 302)


    def test_delete_trip(self):
        """Test: delete a trip"""
        category = Category.objects.create(category_name='Test Category',
                                           slug='test-category')
        trip = Trip.objects.create(name='Test Trip', duration=5,
                                   category=category, slug='test-trip', images='image.jpg')
        found = resolve(f'/trips/delete_trip/{trip.id}/')
        self.assertEqual(found.url_name, "delete_trip")
