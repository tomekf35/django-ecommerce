from django.test import TestCase
from django.contrib.auth import get_user_model
from items.models import Product, Category
from cart.models import CartItem


class CartItemTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.product = Product.objects.create(
            category=self.category,
            brand='Test Brand',
            model='Test Model',
            description='Test Description',
            price=10.0,
            stock=5
        )
        self.cart_item = CartItem.objects.create(user=self.user, product=self.product, quantity=2)

    def tearDown(self):
        self.user.delete()
        self.category.delete()
        self.product.delete()
        self.cart_item.delete()

    def test_total_cost(self):
        expected_total_cost = 20.0
        self.assertEqual(self.cart_item.total_cost, expected_total_cost)

    def test_str_representation(self):
        expected_str_representation = f'{self.user.username} - {self.product.category} {self.product.brand} {self.product.model}'
        self.assertEqual(str(self.cart_item), expected_str_representation)

