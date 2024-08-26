from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Test Item", description="Test Description", quantity=10, price=100.00)

    def test_item_creation(self):
        item = Item.objects.get(name="Test Item")
        self.assertEqual(item.description, "Test Description")
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.price, 100.00)
