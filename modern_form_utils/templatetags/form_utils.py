"""
Template filters for django-modern-form-utils
"""

from django import forms
from django import template
from django.template.loader import render_to_string
from django.template import Context

from ..forms import BetterForm, BetterModelForm
from ..utils import select_template_from_string

register = template.Library()


@register.filter
def render(form, template_name=None):
    """
    Renders a Django Form or BetterForm instance using a template.

    If no template name is provided, it tries:
    - 'form_utils/better_form.html' for BetterForm or BetterModelForm
    - 'form_utils/form.html' otherwise

    If multiple names are passed, it uses select_template().
    """
    default = 'form_utils/form.html'
    if isinstance(form, (BetterForm, BetterModelForm)):
        default = 'form_utils/better_form.html,' + default

    tpl = select_template_from_string(template_name or default)
    return tpl.render(Context({'form': form}))


@register.filter
def label(boundfield, contents=None):
    """Render label tag for a BoundField, optionally with given contents."""
    label_text = contents or boundfield.label
    id_ = boundfield.field.widget.attrs.get('id') or boundfield.auto_id

    return render_to_string("forms/_label.html", {
        "label_text": label_text,
        "id": id_,
        "field": boundfield,
    })


@register.filter
def value_text(boundfield):
    """Return the value for given boundfield as human-readable text."""
    val = boundfield.value()
    choices = getattr(boundfield.field, "choices", [])
    return str(dict(choices).get(val, val))


@register.filter
def selected_values(boundfield):
    """Return selected values of a MultipleChoiceField as human-readable text."""
    val = boundfield.value() or []
    choices = dict(getattr(boundfield.field, "choices", []))
    return [str(choices.get(v, v)) for v in val]


@register.filter
def optional(boundfield):
    """Return True if the field is not required."""
    return not boundfield.field.required


@register.filter
def is_checkbox(boundfield):
    """Return True if this field's widget is a CheckboxInput."""
    return isinstance(boundfield.field.widget, forms.CheckboxInput)


@register.filter
def is_multiple(boundfield):
    """Return True if this field is a MultipleChoiceField."""
    return isinstance(boundfield.field, forms.MultipleChoiceField)


@register.filter
def is_select(boundfield):
    """Return True if this field is a ChoiceField or subclass."""
    return isinstance(boundfield.field, forms.ChoiceField)


@register.filter
def is_radio(boundfield):
    """
    Return True if the widget class name contains 'radio' (case-insensitive).

    This hacky check supports floppyforms and custom widgets that don't inherit
    from Django's built-in RadioSelect.
    """
    return 'radio' in boundfield.field.widget.__class__.__name__.lower()
