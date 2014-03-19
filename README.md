Django Mapped Fields
====================

An set of form fields to make it easier to accept semi-structured data and map
it directly to your own Django Models and Forms


Usage
-----

To use a map field, simply import it and set its `fieldnames` when creating the
field.

```python
from django import forms

from mapped_fields import forms as map


class ContactCsv(forms.Form):
    """Import a Contact from a CSV File.
    """
    first_name = map.Charfield(
        max_length=50, fieldnames=('FirstName', 'Forename'))
    last_name = map.Charfield(
        max_length=50, fieldnames=('LastName', 'Surname'))
    phone_number = map.CharField(
        max_length=30, fieldnames=('Telephone', 'Mobile'))


def map_from_csv():
    csv_files = [
        {
            'FirstName': 'Anne',
            'LastName': 'Other',
            'Mobile': '555-1234',
        },
            'Forename': 'David',
            'Legal Surname': 'Anderson',
            'Telephone': '555-2345',
        },
    ]

    valid_form = ContactCsv(**csv_files[0])
    valid_form.is_valid() == True
    valid_form.cleaned_data['first_name'] == 'Anne'
    valid_form.cleaned_data['last_name'] == 'Other'
    valid_form.cleaned_data['phone_number'] == '555-1234'

    invalid_form = ContactCsv(**csv_files[1])
    invalid_form.is_valid() == False # Legal Surname is not in the mapped fields
```
