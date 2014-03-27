from django.forms import widgets as django_widgets


class MappedWidgetMixin(object):
    """Mixin to override how each widget obtains its value from a datadict.
    """
    def value_from_datadict(self, data, files, name):
        """
        An override to do the field mapping, before calling
        value_from_datadict on super.
        """
        if name not in data:
            mapped_data = self._get_mapped_field_data(data, name)
            return super(MappedWidgetMixin, self).value_from_datadict(
                mapped_data, files, name)

    def _get_mapped_field_data(self, data, name):
        """
        Modify the data dict to only contain values with matching keys.
        Can then be passed to value_from_datadict cleanly.
        """
        mapped_data = {}
        for field_name in self.field_names:
            if field_name in data:
                mapped_data[name] = data[field_name]
                break
        return mapped_data


class MappedTextInput(
        MappedWidgetMixin,
        django_widgets.TextInput):
    pass


class MappedDateInput(
        MappedWidgetMixin,
        django_widgets.DateInput):
    pass


class MappedDateTimeInput(
        MappedWidgetMixin,
        django_widgets.DateTimeInput):
    pass


class MappedNumberInput(
        MappedWidgetMixin,
        getattr(django_widgets, 'NumberInput', django_widgets.TextInput)):
    pass


class MappedCheckboxInput(
        MappedWidgetMixin,
        django_widgets.CheckboxInput):
    pass


class MappedNullBooleanSelect(
        MappedWidgetMixin,
        django_widgets.NullBooleanSelect):
    pass
