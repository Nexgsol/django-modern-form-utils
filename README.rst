# ==================== modern-form-utils

`modern-form-utils` is a modernized fork of the deprecated `django-form-utils` package, updated to support **Django 4.x and 5.x**, and compatible with **Python 3.8+**.

This package provides reusable form enhancements and rendering utilities designed for modern Django projects:

# Features

1. **BetterForm** and **BetterModelForm**:

   - Organize form fields into **fieldsets** for improved layout.
   - Attach **row-level attributes** (e.g. `class`, `style`) to each field.

2. **Template Filters for Forms**:

   - `label` — Custom label rendering.
   - `value_text`, `selected_values` — Display selected choices as text.
   - `optional`, `is_checkbox`, `is_multiple`, `is_select`, `is_radio` — Field-type-aware rendering helpers.

3. **ClearableFileField / ClearableImageField**:

   - Show a checkbox to clear file/image fields at form level.
   - Works out-of-the-box with Django Admin via `ClearableFileFieldsAdmin`.

4. **ImageWidget**:

   - Shows thumbnails for image fields (supports `sorl-thumbnail` or `easy-thumbnails`).

5. **AutoResizeTextarea Widget**:

   - Automatically resizes `<textarea>` based on input.
   - jQuery-based enhancement.

# Installation

```bash
pip install modern-form-utils
```

Then, add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "modern_form_utils",
]
```

If you want to override the default templates, provide your own versions in: `templates/modern_form_utils/better_form.html` and `form.html`.

# Usage

### BetterForm

```python
from modern_form_utils.forms import BetterForm

class MyForm(BetterForm):
    one = forms.CharField()
    two = forms.CharField()
    three = forms.CharField()

    class Meta:
        fieldsets = [
            ("main", {"fields": ["two"], "legend": ""}),
            ("Advanced", {
                "fields": ["three", "one"],
                "description": "Advanced fields",
                "classes": ["advanced", "collapse"]
            }),
        ]
        row_attrs = {
            "one": {"style": "display: none"}
        }
```

### ClearableFileField Example

```python
from modern_form_utils.fields import ClearableFileField

class MyModelForm(forms.ModelForm):
    resume = ClearableFileField()
```

### ImageWidget Example

```python
from modern_form_utils.widgets import ImageWidget

class MyForm(forms.ModelForm):
    avatar = forms.ImageField(widget=ImageWidget())
```

### AutoResizeTextarea Example

```python
from modern_form_utils.widgets import AutoResizeTextarea

class MyForm(forms.Form):
    description = forms.CharField(widget=AutoResizeTextarea())
```

# Template Filters

Load the template filters:

```django
{% load modern_form_utils %}
```

Then use in templates:

```django
{{ form|render }}
{{ form.fieldname|label:"Custom Label" }}
{{ form.fieldname|value_text }}
{% if form.fieldname|is_checkbox %}...{% endif %}
```

# Admin Integration

To make file fields in Django admin clearable:

```python
from modern_form_utils.admin import ClearableFileFieldsAdmin

class MyAdmin(ClearableFileFieldsAdmin):
    pass
```

To use ImageWidget in admin:

```python
class MyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {"widget": ImageWidget},
    }
```

# Settings

### JQUERY\_URL

```python
JQUERY_URL = "https://code.jquery.com/jquery-3.6.0.min.js"
```

If unset, defaults to:

```http
https://ajax.googleapis.com/ajax/libs/jquery/1.8/jquery.min.js
```

# Contributing

- Fork this repo
- Make sure tests pass via `python runtests.py`
- Supports Django 3.2, 4.2, 5.0+ on Python 3.8–3.12

# Credits

Original author: Carl Meyer (django-form-utils)

This package: Updated and maintained by [Muhammed Ziauldin / ziauldin123] under the name `modern-form-utils`.

# License

BSD License (same as the original)

