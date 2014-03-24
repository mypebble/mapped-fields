from django.utils import six

from django.forms import widgets as django_widgets


class MappedWidgetMixinBase(object):
    """
    Abstract base class only for mixins. Identifies subclassed widgets.
    Defines logic common to all inheriting mixins.
    """
    def _get_mapped_field_value(self, data, name):
        """
        Traverses the given data looking for a key match in self.field_names.
        If there's a match, return the value.
        """
        for field_name, value in data.iteritems():
            if field_name in self.field_names:
                return value


class MappedTextInputMixin(MappedWidgetMixinBase):
    """
    Mixin to extend TextInput subclasses with field mapping logic.
    Note that most Widgets extend TextInput, only special cases don't.
    """
    def value_from_datadict(self, data, files, name):
        """An override to do the field mapping
        """
        if name not in data:
            return self._get_mapped_field_value(data, name)


class MappedCheckboxInputMixin(MappedWidgetMixinBase):
    """Mixin just for CheckboxInput widgets.
    """
    def value_from_datadict(self, data, files, name):
        """
        """
        value = self._get_mapped_field_value(data, name)

        # Translate true and false strings to boolean values (from Django).
        values = {'true': True, 'false': False}
        if isinstance(value, six.string_types):
            value = values.get(value.lower(), value)

        return bool(value)


class MappedTextInput(
        MappedTextInputMixin,
        django_widgets.TextInput):
    pass


class MappedDateInput(
        MappedTextInputMixin,
        django_widgets.DateInput):
    pass


class MappedDateTimeInput(
        MappedTextInputMixin,
        django_widgets.DateTimeInput):
    pass


class MappedNumberInput(
        MappedTextInputMixin,
        django_widgets.NumberInput):
    pass


class MappedCheckboxInput(
        MappedCheckboxInputMixin,
        django_widgets.CheckboxInput):
    pass
