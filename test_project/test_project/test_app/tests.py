from datetime import date
from unittest import TestCase

from test_project.test_app import forms


class MappedFieldTestCase(TestCase):
    """Tests to make sure the field mappings all work cleanly.
    """
    def test_valid_contact(self):
        """We can set all the valid fields.
        """
        contact = {
            'FirstName': 'First',
            'Last Name': 'Last',
            'DateOfBirth': '1990-1-11',
            'Tshirts': '15',
        }

        form = forms.ContactForm(data=contact)

        self.assertTrue(form.is_valid())

        self.assertEqual(form.cleaned_data['first_name'], 'First')
        self.assertEqual(form.cleaned_data['last_name'], 'Last')
        self.assertEqual(form.cleaned_data['date_of_birth'], date(1990, 1, 11))
        self.assertEqual(form.cleaned_data['number_of_tshirts'], 15)

    def test_invalid_field(self):
        """The mapped fields work the same way as normal Django Fields.
        """
        contact = {
            'FirstName': 'First',
            'Last Name': 'Last',
            'DateOfBirth': 'Not Valid',
            'Tshirts': '15',
        }

        form = forms.ContactForm(data=contact)

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['date_of_birth'])

    def test_default(self):
        """The default fields work as expected.
        """
        contact = {
            'FirstName': 'First',
            'Last Name': 'Last',
            'DateOfBirth': '1990-1-11',
            'T-Shirts': '100', # T-Shirts is not a pre-set option
        }

        form = forms.ContactForm(data=contact)

        self.assertTrue(form.is_valid())

        self.assertEqual(form.cleaned_data['first_name'], 'First')
        self.assertEqual(form.cleaned_data['last_name'], 'Last')
        self.assertEqual(form.cleaned_data['date_of_birth'], date(1990, 1, 11))
        self.assertEqual(form.cleaned_data['number_of_tshirts'], 0)
