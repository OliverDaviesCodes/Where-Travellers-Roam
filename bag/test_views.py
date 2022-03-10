""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from .views import view_bag, add_to_bag


class TestViews(TestCase):
    """ Tests for bag views """
    def test_bag_url_exists(self):
        """
        Test that bag page URL exists
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)

    def test_bag_view_uses_correct_template(self):
        """
        Test that correct template is used
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='bag/bag.html')

    def test_bag_page_is_accessible_by_name(self):
        """
        test that bag page is accessible by name
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_view_bag(self):
        """
        test that view_bag view works correctly
        """
        link = reverse('view_bag')
        self.assertEqual(resolve(link).func, view_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")

    def test_add_to_bag(self):
        """
        Test that add to bag view works correctly
        """
        link = reverse('add_to_bag', args=['item_id'])
        self.assertEqual(resolve(link).func, add_to_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
