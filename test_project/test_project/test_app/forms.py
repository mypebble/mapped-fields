from django import forms

from mapped_fields import fields


class TestForm(forms.Form):
    """A simple form that we can use to test a range of mapping.
    """
    is_staff = fields.BooleanField(field_names=('staff_member', 'staff'))
    has_file = fields.NullBooleanField(field_names=('documented', 'has_doc'))

    first_name = fields.CharField(
        max_length=50, field_names=('FirstName', 'First Name'))
    last_name = fields.CharField(
        max_length=50, field_names=('LastName', 'Last Name'))

    date_of_birth = fields.DateField(field_names=('DOB', 'DateOfBirth'))

    last_contacted = fields.DateTimeField(
        field_names=('last_contact', 'last_call'))

    height = fields.DecimalField(field_names=('height_m',))

    ratio = fields.FloatField(field_names=('some_ratio',))

    number_of_tshirts = fields.IntegerField(field_names=('Tshirts', ))

    email = fields.EmailField(field_names=('email_address',))

    slug = fields.SlugField(field_names=('reference',))

    url = fields.URLField(field_names=('homepage',))
