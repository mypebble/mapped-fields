Django Mapped Fields
====================
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/mypebble/mapped-fields?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A set of form fields to make it easier to accept semi-structured data with variable (but expected) keys. This data can now be mapped directly to your own Django Models and Forms with normalised field names.

A common use case would be to take CSV or JSON files from external systems and
normalise them into your own data structures.


Usage
-----

To use a map field, simply import it and set its `field_names` when creating the
field.

```python
from django import forms

from mapped_fields import fields


class ContactCsv(forms.Form):
    """Import a Contact from a CSV File.
    """
    first_name = fields.Charfield(
        max_length=50, field_names=('FirstName', 'Forename'))
    last_name = fields.Charfield(
        max_length=50, field_names=('LastName', 'Surname'))
    phone_number = fields.CharField(
        max_length=30, field_names=('Telephone', 'Mobile'))


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

    valid_form = ContactCsv(data=csv_files[0])
    valid_form.is_valid() == True
    valid_form.cleaned_data['first_name'] == 'Anne'
    valid_form.cleaned_data['last_name'] == 'Other'
    valid_form.cleaned_data['phone_number'] == '555-1234'

    invalid_form = ContactCsv(data=csv_files[1])
    invalid_form.is_valid() == False # Legal Surname is not in the mapped fields
```

Handling Multiple field_names in a single file
----------------------------------------------

If you have multiple different fields in the same file mapping to a single
output, the first match on field_names will be used:

```python
from mapped_fields import fields


class ContactForm(forms.Form):
    """Demonstrate multiple field_names.
    """
    name = fields.CharField(
        max_length=100, field_names=('Name', 'ContactName'))


def map_from_dict():
    data = {
        'ContactName': 'James',
        'Name': 'Anderson',
    }

    form = ContactForm(data=data)
    form.is_valid() == True
    form.cleaned_data['name'] == 'Name' # Name was listed first in field_names
```

This is potentially useful if you are importing file formats that are
inconsistent, and where you want a fallback if the "best" header isn't
there.


Fields
------

The Mapped Fields plugin works by extending existing django fields. The
currently supported fields are:

- `mapped_fields.fields.BooleanField`
- `mapped_fields.fields.NullBooleanField`
- `mapped_fields.fields.CharField`
- `mapped_fields.fields.DateField`
- `mapped_fields.fields.DateTimeField`
- `mapped_fields.fields.DecimalField`
- `mapped_fields.fields.FloatField`
- `mapped_fields.fields.IntegerField`
- `mapped_fields.fields.EmailField`
- `mapped_fields.fields.SlugField`
- `mapped_fields.fields.URLField`


All fields work as in Django, but take a mandatory extra argument `field_names` -- a list or tuple
of field names to map from the source data into the field.


Testing
-------

To test, install the requirements inside your virtualenv then run test
inside test_project:

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python setup.py install

cd test_project
./manage.py test
```
