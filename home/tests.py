from django.test import TestCase


class TestHomeView(TestCase):
    """Unit Test for home view"""

    def test_home_view(self):
        """Test HTTP response"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
