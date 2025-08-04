"""
Utility functions for django-modern-form-utils
"""

from django.template import loader


def select_template_from_string(template_string: str):
    """
    Given a comma-separated string of template names, returns the first found template.

    Args:
        template_string (str): A single template name or comma-separated list.

    Returns:
        Template object from Django's template loader.
    """
    if ',' in template_string:
        template_names = [name.strip() for name in template_string.split(',')]
        return loader.select_template(template_names)
    return loader.get_template(template_string)
