from django.forms import widgets as django_widgets


class MappedWidgetMixinBase(object):
    """Abstract base class only for mixins. Identifies subclassed widgets.
    """
    pass


class MappedTextInputMixin(MappedWidgetMixinBase):
    """
    Mixin to extend TextInput subclasses with field mapping logic.
    Note that most Widgets extend TextInput, only special cases don't.
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


class MappedCheckboxInputMixin(MappedWidgetMixinBase):
    """
    """
    pass


class MappedTextInput(
        MappedTextInputMixin,
        django_widgets.TextInput):
    """
    """
    pass


class MappedDateInput(
        MappedTextInputMixin,
        django_widgets.DateInput):
    """
    """
    pass


class MappedNumberInput(
        MappedTextInputMixin,
        django_widgets.NumberInput):
    """
    """
    pass
