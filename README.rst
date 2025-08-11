==============================
django-modern-form-utils
==============================

``django-modern-form-utils`` is a modernized fork of the deprecated ``django-form-utils`` package, updated to support **Django 4.x and 5.x**, and compatible with **Python 3.8+**.

This package provides reusable form enhancements and rendering utilities designed for modern Django projects.

Features
========

1. **BetterForm** and **BetterModelForm**:
   - Organize form fields into **fieldsets** for improved layout.
   - Attach **row-level attributes** (e.g. ``class``, ``style``) to each field.

2. **Template Filters for Forms**:
   - ``label`` — Custom label rendering.
   - ``value_text``, ``selected_values`` — Display selected choices as text.
   - ``optional``, ``is_checkbox``, ``is_multiple``, ``is_select``, ``is_radio`` — Field-type-aware rendering helpers.

3. **ClearableFileField / ClearableImageField**:
   - Show a checkbox to clear file/image fields at form level.
   - Works out-of-the-box with Django Admin via ``ClearableFileFieldsAdmin``.

4. **ImageWidget**:
   - Shows thumbnails for image fields (supports ``sorl-thumbnail`` or ``easy-thumbnails``).

5. **AutoResizeTextarea Widget**:
   - Automatically resizes ``<textarea>`` based on input.
   - jQuery-based enhancement.

Installation
============

.. code-block:: bash

   pip install django-modern-form-utils

Then, add it to your ``INSTALLED_APPS``:

.. code-block:: python

   INSTALLED_APPS = [
       ...
       "modern_form_utils",
   ]

If you want to override the default templates, provide your own versions in:
``templates/modern_form_utils/better_form.html`` and ``form.html``.

Usage
=====

BetterForm Example
------------------

.. code-block:: python

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

ClearableFileField Example
--------------------------

.. code-block:: python

   from modern_form_utils.fields import ClearableFileField

   class MyModelForm(forms.ModelForm):
       resume = ClearableFileField()

ImageWidget Example
-------------------

.. code-block:: python

   from modern_form_utils.widgets import ImageWidget

   class MyForm(forms.ModelForm):
       avatar = forms.ImageField(widget=ImageWidget())

AutoResizeTextarea Example
--------------------------

.. code-block:: python

   from modern_form_utils.widgets import AutoResizeTextarea

   class MyForm(forms.Form):
       description = forms.CharField(widget=AutoResizeTextarea())

Template Filters
================

Load the template filters:

.. code-block:: django

   {% load modern_form_utils %}

Then use in templates:

.. code-block:: django

   {{ form|render }}
   {{ form.fieldname|label:"Custom Label" }}
   {{ form.fieldname|value_text }}
   {% if form.fieldname|is_checkbox %}...{% endif %}

Admin Integration
=================

To make file fields in Django admin clearable:

.. code-block:: python

   from modern_form_utils.admin import ClearableFileFieldsAdmin

   class MyAdmin(ClearableFileFieldsAdmin):
       pass

To use ImageWidget in admin:

.. code-block:: python

   class MyAdmin(admin.ModelAdmin):
       formfield_overrides = {
           models.ImageField: {"widget": ImageWidget},
       }

Settings
========

JQUERY\_URL
-----------

.. code-block:: python

   JQUERY_URL = "https://code.jquery.com/jquery-3.6.0.min.js"

If unset, defaults to:

::

   https://ajax.googleapis.com/ajax/libs/jquery/1.8/jquery.min.js

Contributing
============

- Fork this repo
- Make sure tests pass via ``python runtests.py``
- Supports Django 3.2, 4.2, 5.0+ on Python 3.8–3.12

Credits
=======

Original author: **Carl Meyer** (django-form-utils)

This package: Updated and maintained by **Muhammad Ziauldin**

GitHub: https://github.com/ziauldin123

Organization: https://github.com/Nexgsol

Package: ``django-modern-form-utils``

License
=======

BSD License (same as the original)
