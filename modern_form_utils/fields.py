"""
Custom form fields for django-modern-form-utils
"""

from django import forms
from .widgets import ClearableFileInput


class FakeEmptyFieldFile:
    """
    A fake FieldFile that convinces a FileField to replace an existing filename with an empty string.

    Django's FileField only updates its value if the incoming data is truthy. This prevents clearing
    via empty input. This object evaluates truthy, but stringifies to empty string.

    It's used to bypass that logic and trigger clearing of the field without needing a model subclass.

    WARNING: This is a hack and relies on internal Django behavior. Use with care.
    """

    def __str__(self):
        return ''

    _committed = True


class ClearableFileField(forms.MultiValueField):
    """
    A file input field with an additional checkbox to clear the current file.
    """
    default_file_field_class = forms.FileField
    widget = ClearableFileInput

    def __init__(self, file_field=None, template=None, *args, **kwargs):
        file_field = file_field or self.default_file_field_class(*args, **kwargs)
        fields = (file_field, forms.BooleanField(required=False))
        kwargs['required'] = file_field.required
        kwargs['widget'] = self.widget(
            file_widget=file_field.widget,
            template=template
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        """
        If the clear checkbox is checked and no new file is uploaded, return FakeEmptyFieldFile.
        Otherwise return the uploaded file.
        """
        if data_list[1] and not data_list[0]:
            return FakeEmptyFieldFile()
        return data_list[0]


class ClearableImageField(ClearableFileField):
    """
    A ClearableFileField configured for image input.
    """
    default_file_field_class = forms.ImageField
