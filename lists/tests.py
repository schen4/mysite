from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item
from test.test_pydoc import expected_data_docstrings
from django.template.context_processors import request



# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    """
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        #print(response.content)
        expect_html = render_to_string('home.html',
            {'new_item_text': 'A new list item'}
        )
        #self.assertEqual(response.content.decode(), expect_html)
        
        #self.assertTrue(response.content.start(b'<html>'))
        #self.assertIn(b'<title>To-Do lists</title>', response.content)
        #self.assertTrue(response.content.end_string(b'</html>'))
    """
    
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        
    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item_text = 'The first list item'
        first_item.save()
        