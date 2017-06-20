from django.test import Client, TestCase, RequestFactory
from django.urls import reverse
from lending_library.views import home_view


class ViewTests(TestCase):
    """."""

    def setUp(self):
        """."""
        self.client = Client()
        self.get_request = RequestFactory().get('/foo')

    def test_home_route_returns_status_200(self):
        """."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_does_something(self):
        """."""
        response = home_view(self.get_request)
        self.assertTrue(b'h1' in response.content)
