from __future__ import unicode_literals

from rest_framework.renderers import  JSONRenderer

class JSONURenderer(JSONRenderer):
    """
    Renderer which serializes to JSON.
    Applies JSON's backslash-u character escaping for non-ascii characters.
    """
    ensure_ascii = False
    charset = 'utf-8'
