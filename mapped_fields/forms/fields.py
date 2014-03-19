import types

from django import forms


def _value_from_datadict(self, data, files, name):
    """Run through the given field names. If we have a match in data, then
    return the value given.
    """


class MappedFieldMixin(object):
    def __init__(self, field_names, *args, **kwargs):
        self.field_names = field_names
        super(MappedFieldMixin, self).__init__(*args, **kwargs)
        self.widget.field_names = self.field_names
        self.widget.value_from_datadict = types.MethodType(
            _value_from_datadict, self.widget.__class__)
