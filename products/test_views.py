""" Testing code adapted from Code Institute BoutiqueAdo project """
from django.test import TestCase
from django.shortcuts import reverse

from .models import Product


class TestViews(TestCase):
    """ Tests for product views """
    def test_product_page_url_exists(self):
        """
        Test that the blog page URL exists
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_view_uses_correct_template(self):
        """
        Test correct template is used
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='products/products.html')

    def test_product_page_is_accessible_by_name(self):
        """
        test product page is accessible by name
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_products(self):
        """
        Test that a product can be retrieved
        """
        products = Product.objects.all()
        for product in products:
            response = self.client.get(reverse('products'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, product.id)

    def test_product_detail_page_url_exists(self):
        """
        test product detail page loads via url
        """
        product = Product.objects.create(id='9', name='test',
                                         description='test', price='9.99')
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_template(self):
        """
        test product detail page loads via template
        """
        product = Product.objects.create(id='9', name='test',
                                         description='test', price='9.99')
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
