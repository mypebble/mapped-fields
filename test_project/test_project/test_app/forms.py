from django import forms

from mapped_fields import forms as maps


class ContactForm(forms.Form):
    """A simple contact form that we can use to test a range of mapping.
    """
    first_name = maps.CharField(
        max_length=50, field_names=('FirstName', 'First Name'))
    last_name = maps.CharField(
        max_length=50, field_names=('LastName', 'Last Name'))

    date_of_birth = maps.DateField(field_names=('DOB', 'DateOfBirth'))

    number_of_tshirts = maps.IntegerField(field_names=('Tshirts', ), default=0)
