""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from .models import Category, Product


class TestCategoryModel(TestCase):
    """ test category model """
    def test_category_string_method(self):
        """
        test category model string method
        """
        category = Category.objects.create(name="test_category")
        self.assertEqual(str(category), "test_category")

    def test_category_friendly_name_string_method(self):
        """
        test category model friendly name string method
        """
        test_case = Category()
        test_case.friendly_name = "test"
        self.assertEqual(test_case.get_friendly_name(), "test")
