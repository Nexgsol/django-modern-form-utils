from django.contrib import admin
from django import forms
from .fields import ClearableFileField


class ClearableFileFieldsAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = db_field.formfield(**kwargs)
        if isinstance(formfield, forms.FileField):
            return ClearableFileField()
        return super().formfield_for_dbfield(db_field, request, **kwargs)
