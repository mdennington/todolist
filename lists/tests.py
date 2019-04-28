# resolve is function used by Django to 
# resolve URLS and find the view function they map to
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

# Deleted as not required
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

# Create http object, pass to home page 
# view and check html that returns
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # These are the long way of achieving what the DjangoTestClient 
        # provides. Better to validate template used for given URL
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To Do Lists</title>', html)
        # self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')

    

