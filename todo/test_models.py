from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    # test if done status is False by default
    def test_done_defaults_to_false(self):
        # create test item
        item = Item.objects.create(name='Test Todo Item')
        # check if status of done field is False
        self.assertFalse(item.done)

    # test the string method
    def test_item_string_method_returns_name(self):
        # create test item
        item = Item.objects.create(name='Test Todo Item')
        # check if test item is a String
        self.assertEqual(str(item), 'Test Todo Item')
