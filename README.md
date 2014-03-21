Django Mapped Fields
====================

A set of form fields to make it easier to accept semi-structured data and map
it directly to your own Django Models and Forms.

A common use case would be to take CSV or JSON files from external systems and
normalise them into your own data structures.


Usage
-----

To use a map field, simply import it and set its `field_names` when creating the
field.

```python
from django import forms

from mapped_fields import forms as maps


class ContactCsv(forms.Form):
    """Import a Contact from a CSV File.
    """
    first_name = maps.Charfield(
        max_length=50, field_names=('FirstName', 'Forename'))
    last_name = maps.Charfield(
        max_length=50, field_names=('LastName', 'Surname'))
    phone_number = maps.CharField(
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


Fields
------

The Mapped Fields plugin works by extending existing django fields. The
currently supported fields are:

- `mapped_fields.forms.BooleanField`
- `mapped_fields.forms.CharField`
- `mapped_fields.forms.DateField`
- `mapped_fields.forms.DateTimeField`
- `mapped_fields.forms.DecimalField`
- `mapped_fields.forms.EmailField`
- `mapped_fields.forms.FloatField`
- `mapped_fields.forms.IntegerField`
- `mapped_fields.forms.SlugField`
- `mapped_fields.forms.URLField`


All fields work as in Django, but take a mandatory extra argument `field_names`


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
