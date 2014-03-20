from django import forms

from mapped_fields import widgets as mapped_widgets


class MappedFieldMixin(object):
    """
    """

    def __init__(self, field_names, **kwargs):
        """
        """
        super(MappedFieldMixin, self).__init__(**kwargs)
        self.widget.field_names = field_names
        print self.widget, field_names


class CharField(MappedFieldMixin, forms.CharField):
    """
    """
    widget = mapped_widgets.MappedTextInput


class DateField(MappedFieldMixin, forms.DateField):
    """
    """
    widget = mapped_widgets.MappedDateInput


class IntegerField(MappedFieldMixin, forms.IntegerField):
    """
    """
    widget = mapped_widgets.MappedNumberInput
