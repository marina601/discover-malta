from django.test import TestCase
from .forms import ReviewForm, TripForm
from django.shortcuts import get_object_or_404

from .models import Category

# Create your tests here.


class TestTripForm(TestCase):
    """Test Trip Form"""

    def test_fields_is_required(self):
        """Test to check the fields are required"""
        form = TripForm({
                        'name': '',
                        'category': '',
                        'short_description': '',
                        'full_description': '',
                        'included': '',
                        'what_to_bring': '',
                        'duration': '',
                        'start_time': '',
                        'departure_location': '',
                        'family_friendly': '',
                        'adult_price': '',
                        'child_price': '',
                        'images': '',
                        'num_tickets': '',
                        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertIn('short_description', form.errors.keys())
        self.assertEqual(form.errors['short_description'][0],
                         'This field is required.')
        self.assertIn('full_description', form.errors.keys())
        self.assertEqual(form.errors['full_description'][0],
                         'This field is required.')
        self.assertIn('duration', form.errors.keys())
        self.assertEqual(form.errors['duration'][0], 'This field is required.')
        self.assertIn('departure_location', form.errors.keys())
        self.assertEqual(form.errors['departure_location'][0],
                         'This field is required.')
        self.assertIn('images', form.errors.keys())
        self.assertEqual(form.errors['images'][0], 'This field is required.')
        self.assertIn('num_tickets', form.errors.keys())
        self.assertEqual(form.errors['num_tickets'][0],
                         'This field is required.')

    # def test_field_is_not_required(self):
    #     """Test Fields are not required"""
    #     form = TripForm({
    #                     'name': 'Cuba',
    #                     'category': 'fishing',
    #                     'short_description': 'This is a test',
    #                     'full_description': 'This is a long test',
    #                     'included': 'nothing',
    #                     'what_to_bring': 'money',
    #                     'duration': '5',
    #                     'start_time': '08:00',
    #                     'departure_location': 'Valetta',
    #                     'family_friendly': True,
    #                     'adult_price': '12.0',
    #                     'child_price': '0.0',
    #                     'images': 'media/trips/image.png',
    #                     'num_tickets': '10',
    #                     })
    #     self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """Test the form fields match"""
        form = TripForm()
        self.assertEqual(form.Meta.fields, ['name', 'category',
                                            'short_description',
                                            'full_description', 'included',
                                            'what_to_bring',
                                            'duration', 'start_time',
                                            'departure_location',
                                            'family_friendly',
                                            'adult_price', 'child_price',
                                            'images',
                                            'num_tickets'])


class TestReviewForm(TestCase):
    """Test Review Form"""
    def test_required_fields_in_review_form(self):
        """Test required fields in the review form"""
        form = ReviewForm({
            'subject': '',
            'review': '',
            'rating': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(form.errors['subject'][0], 'This field is required.')
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_not_required_fields_in_review_form(self):
        """Test required fields in the review form"""
        form = ReviewForm({
            'subject': 'Test',
            'review': '',
            'rating': '2.5',
        })
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """Test the form fields match"""
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ['subject', 'review', 'rating'])
