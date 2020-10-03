from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    # function to test if the form returns errors if the required
    # field name is not filled in
    def test_item_name_is_required(self):
        # assign the form field name with no value
        form = ItemForm({'name': ''})
        # check if the form is valid returns false --> yes, so the test passes
        self.assertFalse(form.is_valid())
        # check if there is a name key in the returned error message
        self.assertIn('name', form.errors.keys())
        # check if the error message is the one for field required
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # function to test if the done field is not required
    def test_done_field_is_not_required(self):
        # assigns a form with filled name field, so requirement should be met
        form = ItemForm({'name': 'Test Todo Item'})
        # check if the form is valid, it should be because doneis not required
        self.assertTrue(form.is_valid())

    # function to check if only the fields name and done are displayed
    def test_fields_are_explicit_in_form_metaclass(self):
        # assign ItemForm from forms.py to variable form
        form = ItemForm()
        # check if the displayed fields are equal to name and done
        self.assertEqual(form.Meta.fields, ['name', 'done'])
