"""
Custom form fields for django-modern-form-utils
"""

from django import forms
from django.utils.safestring import mark_safe
from .widgets import ClearableFileInput


class FakeEmptyFieldFile:
    """
    A fake FieldFile that convinces a FileField to replace an existing filename with an empty string.
    Django's FileField only updates its value if the incoming data is truthy. This prevents clearing
    via empty input. This object evaluates truthy, but stringifies to empty string.

    WARNING: This is a hack and relies on internal Django behavior. Use with care.
    """

    def __str__(self):
        return ''
    
    @property 
    def name(self):
        return ''
    
    @property
    def url(self):
        return ''
    
    _committed = True
    _file = None
    size = 0

    def save(self, *args, **kwargs):
        return ''

    def delete(self, *args, **kwargs):
        pass


class ClearableFileField(forms.MultiValueField):
    """
    A file input field with an additional checkbox to clear the current file.
    """
    default_file_field_class = forms.FileField
    widget = ClearableFileInput

    def __init__(self, file_field=None, template=None, *args, **kwargs):
        file_field = file_field or self.default_file_field_class(*args, **kwargs)
        
        # Store the original widget before creating the MultiWidget
        self.original_widget = file_field.widget
        
        fields = (
            file_field,
            forms.BooleanField(
                required=False,
                label="Clear"
            )
        )
        
        kwargs['required'] = file_field.required
        kwargs['widget'] = self.widget(
            file_widget=self.original_widget,  # Preserve original widget
            template=template
        )
        
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        """
        If the clear checkbox is checked and no new file is uploaded, return FakeEmptyFieldFile.
        Otherwise return the uploaded file.
        """
        if data_list and len(data_list) > 1:
            if data_list[1] and not data_list[0]:
                return FakeEmptyFieldFile()
            return data_list[0]
        return None

    def clean(self, value):
        """
        Handle cleaning while preserving the original field's cleaning behavior
        """
        if value and isinstance(value, list) and len(value) > 1:
            if value[1]:  # Clear checkbox was checked
                if not value[0]:  # No new file uploaded
                    return FakeEmptyFieldFile()
        return super().clean(value)


class ClearableImageField(ClearableFileField):
    """
    A ClearableFileField configured for image input.
    """
    default_file_field_class = forms.ImageField

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure the original widget is preserved for image-specific attributes
        if hasattr(self, 'original_widget'):
            self.widget.widgets[0] = self.original_widget