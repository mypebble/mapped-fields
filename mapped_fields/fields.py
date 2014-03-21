from django import forms

from mapped_fields import widgets as mapped_widgets


class MappedFieldMixin(object):
    """Mixin for each mapped field subclass
    """
    def __init__(self, field_names, **kwargs):
        """
        Override to force the correct widget and set field_names on it,
        when a widget inheriting MappedWidgetMixinBase is used.

        Leaves widget alone if passed in kwargs (widget class must still
        implement logic from mixin in order to work as expected).
        """
        default_override = (
            'widget' not in kwargs and
            issubclass(self.widget, mapped_widgets.MappedWidgetMixinBase))

        if default_override:
            kwargs['widget'] = self.widget

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
