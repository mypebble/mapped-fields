from django.forms import widgets as django_widgets


class MappedFieldWidgetMixin(object):
    """Mixin to extend each Django Widget subclass with field mapping logic.
    """
    def value_from_datadict(self, data, files, name):
        """
        An override to do the mapping, by traversing the given data if the
        field name itself isn't present as a key.
        If there's a match in self.field_names, return the value.
        """
        if name not in data:
            for field_name, value in data.iteritems():
                if field_name in self.field_names:
                    return value


class MappedTextInput(
        MappedFieldWidgetMixin,
        django_widgets.TextInput):
    """
    """
    pass


class MappedDateInput(
        MappedFieldWidgetMixin,
        django_widgets.DateInput):
    """
    """
    pass


class MappedNumberInput(
        MappedFieldWidgetMixin,
        django_widgets.NumberInput):
    """
    """
    pass
