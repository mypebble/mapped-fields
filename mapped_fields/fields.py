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

    def __init__(self, *args, **kwargs):
        default_override = (
            self.widget == mapped_widgets.MappedNumberInput
            and 'widget' not in kwargs)
        if default_override:
            kwargs['widget'] = self.widget

        super(IntegerField, self).__init__(*args, **kwargs)

