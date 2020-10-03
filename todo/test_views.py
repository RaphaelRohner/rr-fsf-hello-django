from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    # test to check if the view get_todo_list works
    def test_get_todo_list(self):
        # assign the homepage
        response = self.client.get('/')
        # checks if the response code is 200 meaning ok
        self.assertEqual(response.status_code, 200)
        # checks if the page loaded is todo_list.html
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # test to check if the view add_item works
    def test_get_add_item_page(self):
        # assign the add page
        response = self.client.get('/add')
        # checks if the response code is 200 meaning ok
        self.assertEqual(response.status_code, 200)
        # checks if the page loaded is add_item.html
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # test to check if the view edit_item works
    # Item needs to be imported for this
    def test_get_edit_item_page(self):
        # create an item to test if it can be edited
        item = Item.objects.create(name='Test Todo Item')
        # assign the edit page
        response = self.client.get(f'/edit/{item.id}')
        # checks if the response code is 200 meaning ok
        self.assertEqual(response.status_code, 200)
        # checks if the page loaded is edit_item.html
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # test to check if item can be added
    def test_can_add_item(self):
        # add an item
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # check if the response redirects to the homepage
        self.assertRedirects(response, '/')

    # test to check if item can be deleted
    def test_can_delete_item(self):
        # create an item to test if it can be deleted
        item = Item.objects.create(name='Test Todo Item')
        # assign the edit page
        response = self.client.get(f'/delete/{item.id}')
        # check if the response redirects to the homepage
        self.assertRedirects(response, '/')
        # assign Item objects to var
        existing_items = Item.objects.filter(id=item.id)
        # check if the variables length is 0. One item added and delted
        self.assertEqual(len(existing_items), 0)

    # test to check if item status can be toggled
    def test_can_toggle_item(self):
        # create an item to test if status can be toggled
        item = Item.objects.create(name='Test Todo Item', done=True)
        # assign the toggle view
        response = self.client.get(f'/toggle/{item.id}')
        # check if the response redirects to the homepage
        self.assertRedirects(response, '/')
        # assign item to new variable
        updated_item = Item.objects.get(id=item.id)
        # check if the status has changed to False
        self.assertFalse(updated_item.done)

    # test to check if item status can be toggled
    def test_can_edit_item(self):
        # create an item to test if it can be edited
        item = Item.objects.create(name='Test Todo Item')
        # run the edit view
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        # check if the response redirects to the homepage
        self.assertRedirects(response, '/')
        # assign item to new variable
        updated_item = Item.objects.get(id=item.id)
        # check if the content of name has changed to the new value
        self.assertEqual(updated_item.name, 'Updated Name')
