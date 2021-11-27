from django.test import TestCase


class TestContactView(TestCase):

    def test_contact_view(self):
        """Test HTTP of contact view response"""
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
    
    def test_about_view(self):
        """Test HTTP of about view response"""
        response = self.client.get('/contact/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')