"""
Admin integration for ClearableFileField in django-modern-form-utils
"""

from django.contrib import admin
from django import forms

from .fields import ClearableFileField


class ClearableFileFieldsAdmin(admin.ModelAdmin):
    """
    A ModelAdmin that automatically replaces FileFields with ClearableFileField in the admin form.
    """
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if isinstance(field, forms.FileField):
            field = ClearableFileField(file_field=field)
        return field
