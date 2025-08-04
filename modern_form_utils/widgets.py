"""
Widgets for django-modern-form-utils

Parts of this code are inspired by http://www.djangosnippets.org/snippets/934/
Thanks to baumer1122.
"""

import posixpath
from typing import Optional

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from .settings import JQUERY_URL

# Thumbnail rendering (try sorl, easy_thumbnails, fallback to basic img)
try:
    from sorl.thumbnail import get_thumbnail

    def thumbnail(image_path, width, height):
        geometry = f"{width}x{height}"
        t = get_thumbnail(image_path, geometry)
        return f'<img src="{t.url}" alt="{image_path}" />'

except ImportError:
    try:
        from easy_thumbnails.files import get_thumbnailer

        def thumbnail(image_path, width, height):
            opts = dict(size=(width, height), crop=True)
            thumb = get_thumbnailer(image_path).get_thumbnail(opts)
            return f'<img src="{thumb.url}" alt="{image_path}" />'

    except ImportError:
        def thumbnail(image_path, width, height):
            url = posixpath.join(settings.MEDIA_URL, image_path)
            return f'<img src="{url}" alt="{image_path}" />'


class ImageWidget(forms.FileInput):
    def __init__(
        self,
        attrs: Optional[dict] = None,
        template: Optional[str] = None,
        width: int = 200,
        height: int = 200,
    ):
        self.template = template or "%(input)s<br />%(image)s"
        self.width = width
        self.height = height
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs, renderer)
        if hasattr(value, 'width') and hasattr(value, 'height'):
            image_html = thumbnail(value.name, self.width, self.height)
            output = self.template % {'input': input_html, 'image': image_html}
        else:
            output = input_html
        return mark_safe(output)


class ClearableFileInput(forms.MultiWidget):
    default_file_widget_class = forms.FileInput
    template = '%(input)s Clear: %(checkbox)s'

    def __init__(self, file_widget=None, attrs=None, template=None):
        self.template = template or self.template
        file_widget = file_widget or self.default_file_widget_class()
        widgets = [file_widget, forms.CheckboxInput()]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        return [value, None]

    def render(self, name, value, attrs=None, renderer=None):
        if isinstance(value, list):
            self.value = value[0]
        else:
            self.value = value
        rendered = super().render(name, value, attrs, renderer)
        if self.value:
            input_html = self.widgets[0].render(f"{name}_0", self.value, attrs, renderer)
            checkbox_html = self.widgets[1].render(f"{name}_1", False, attrs, renderer)
            return mark_safe(self.template % {
                'input': input_html,
                'checkbox': checkbox_html,
            })
        return self.widgets[0].render(f"{name}_0", value, attrs, renderer)


def root(path: str) -> str:
    return posixpath.join(settings.STATIC_URL, path)


class AutoResizeTextarea(forms.Textarea):
    """
    A Textarea widget that automatically resizes to accommodate its contents.
    """

    class Media:
        js = (
            JQUERY_URL,
            root('form_utils/js/jquery.autogrow.js'),
            root('form_utils/js/autoresize.js'),
        )

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs['class'] = f"{attrs.get('class', '')} autoresize".strip()
        attrs.setdefault('cols', 80)
        attrs.setdefault('rows', 5)
        super().__init__(*args, **kwargs)


class InlineAutoResizeTextarea(AutoResizeTextarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs['class'] = f"{attrs.get('class', '')} inline".strip()
        attrs.setdefault('cols', 40)
        attrs.setdefault('rows', 2)
        super().__init__(*args, **kwargs)
