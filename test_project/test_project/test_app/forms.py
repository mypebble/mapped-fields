from django import forms

from mapped_fields import fields


class ContactForm(forms.Form):
    """A simple contact form that we can use to test a range of mapping.
    """
    first_name = fields.CharField(
        max_length=50, field_names=('FirstName', 'First Name'))
    last_name = fields.CharField(
        max_length=50, field_names=('LastName', 'Last Name'))

    date_of_birth = fields.DateField(field_names=('DOB', 'DateOfBirth'))

    number_of_tshirts = fields.IntegerField(field_names=('Tshirts', ))
