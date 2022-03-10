""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase

from .templatetags.bag_tools import calc_subtotal


class TestBagTools(TestCase):
    """ Test the bag tools calc_subtotal function """
    def test_calc_subtotal(self):
        """ Test that the calc_subtotal function works"""
        self.assertEqual(calc_subtotal(9.99, 2), 19.98)
        self.assertNotEqual(calc_subtotal(19.99, 3), 49.97)
