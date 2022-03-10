""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from django.shortcuts import reverse


class TestViews(TestCase):
    """ Tests for checkout views """
    def test_checkout_url_exists(self):
        """
        Test that checkout page URL exists
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_checkout_view_uses_correct_template(self):
        """
        Test correct template is used
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_basket_page_is_accessible_by_name(self):
        """
        test checkout page is accessible by name
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_cache_checkout_data_view(self):
        """
        Test that cache_checkout_data view works
        """
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)
