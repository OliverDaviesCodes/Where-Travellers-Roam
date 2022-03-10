""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from django.shortcuts import reverse


class TestViews(TestCase):
    """ Tests for homepage """
    def test_homepage_url_exists(self):
        """
        Test that homepage URL exists
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        """
        Test the correct template is used
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='home/index.html')

    def test_homepage_is_accessible_by_name(self):
        """
        test homepage is accessible by name
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
