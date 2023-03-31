from django.test import TestCase
from restaurant.models import Menu

class MenuItemTestcase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, item)