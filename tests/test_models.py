from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    """This class is for test different
    methods of Menu entity"""
    def test_get_menu(self):
        """This method create a menu and call the get_item method
        and then do a comparation using the assertEqual method"""
        item = Menu.objects.create(title="Helado de Vainilla", price=80, inventory=100)
        item_str = item.get_item()

        self.assertEqual(item_str, "Helado de Vainilla : 80")
