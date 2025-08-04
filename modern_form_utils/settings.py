import os
import posixpath
from django.conf import settings

# Default jQuery URL (CDN), overrideable via Django project settings
JQUERY_URL = getattr(
    settings,
    'JQUERY_URL',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js'
)

# Normalize to absolute path if it's a relative path
if not (':' in JQUERY_URL or JQUERY_URL.startswith('/')):
    JQUERY_URL = posixpath.join(settings.STATIC_URL, JQUERY_URL)
