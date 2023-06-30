from django.test import TestCase
from .models import Category, Product

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
    
    def tearDown(self):
        self.category.delete()
    
    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.description, 'Test Description')
    
    def test_str_representation(self):
        expected_str_representation = 'Test Category'
        self.assertEqual(str(self.category), expected_str_representation)


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.product = Product.objects.create(
            category=self.category,
            brand='Test Brand',
            model='Test Model',
            description='Test Description',
            price=10.0,
            image='test_image.jpg',
            stock=10
        )
    
    def tearDown(self):
        self.product.delete()
        self.category.delete()
    
    def test_product_creation(self):
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.brand, 'Test Brand')
        self.assertEqual(self.product.model, 'Test Model')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.price, 10.0)
        self.assertEqual(self.product.image, 'test_image.jpg')
        self.assertEqual(self.product.stock, 10)
    
    def test_str_representation(self):
        expected_str_representation = 'Test Category Test Brand Test Model'
        self.assertEqual(str(self.product), expected_str_representation)

