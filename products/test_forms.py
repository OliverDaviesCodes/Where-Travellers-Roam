""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """ Tests for product form """
    def test_sku_is_not_required(self):
        """ Test sku field is not required """
        form = ProductForm({'sku': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('sku', form.errors.keys())

    def test_name_is_required(self):
        """ Test name field is required """
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
                         form.errors['name'][0],
                         'This field is required.'
        )

    def test_description_is_required(self):
        """ Test description field is required """
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
                         form.errors['description'][0],
                         'This field is required.'
        )

    def test_price_is_required(self):
        """ Test price field is required """
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
                         form.errors['price'][0],
                         'This field is required.'
        )

    def test_image_field_is_not_required(self):
        """ Test image field is not required """
        form = ProductForm({'image_field': ''})
        self.assertFalse(form.is_valid())
        self.assertNotIn('image_field', form.errors.keys())
