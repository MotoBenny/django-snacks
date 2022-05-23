from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
# python3 manage.py test


class SnacksTest(SimpleTestCase):
    def tests_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def tests_about_page_status(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')

    def test_not_found(self):
        url = 'kitten/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
