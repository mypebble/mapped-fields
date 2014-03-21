from datetime import date
from unittest import TestCase

import mapped_fields

from test_project.test_app import forms


class MappedFieldTestCase(TestCase):
    """Tests to make sure the field mappings all work cleanly.
    """
    def test_widget_inheritance(self):
        """The correct Widget subclasses are used.
        """
        form = forms.TestForm()

        self.assertTrue(isinstance(
            form.fields['first_name'].widget,
            mapped_fields.widgets.MappedTextInput))

        self.assertTrue(isinstance(
            form.fields['last_name'].widget,
            mapped_fields.widgets.MappedTextInput))

        self.assertTrue(isinstance(
            form.fields['date_of_birth'].widget,
            mapped_fields.widgets.MappedDateInput))

        self.assertTrue(isinstance(
            form.fields['number_of_tshirts'].widget,
            mapped_fields.widgets.MappedNumberInput))

    def test_valid_contact(self):
        """We can set all the valid fields.
        """
        contact = {
            'FirstName': 'First',
            'Last Name': 'Last',
            'DateOfBirth': '1990-1-11',
            'Tshirts': '15',
        }

        form = forms.TestForm(data=contact)

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

        form = forms.TestForm(data=contact)

        field_errors = (
            'is_staff',
            'date_of_birth',
        )

        self.assertFalse(form.is_valid())

        for field in field_errors:
            self.assertTrue(field in form.errors,
                '{} not in errors list'.format(field))
