# resolve is function used by Django to 
# resolve URLS and find the view function they map to
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item

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


    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
       
    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text':'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='Item 1')
        Item.objects.create(text='Item 2')

        response = self.client.get('/')

        self.assertIn('Item 1', response.content.decode())
        self.assertIn('Item 2', response.content.decode())
        

